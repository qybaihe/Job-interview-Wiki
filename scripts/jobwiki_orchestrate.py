#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / 'controller' / 'progress_state.json'
FIRST_BATCH_PATH = ROOT / 'FIRST_BATCH.md'

TARGETS = [
    {
        'company': '字节跳动',
        'business_group': '抖音电商',
        'department': '商业化技术',
        'role': '后端开发',
        'question_bank': ROOT / 'companies' / '字节跳动' / '抖音电商' / '商业化技术' / 'question-bank.md',
        'json_dir': ROOT / 'companies' / '字节跳动' / '抖音电商' / '商业化技术' / 'interview-experiences',
    },
    {
        'company': '腾讯',
        'business_group': '微信事业群',
        'department': '基础平台',
        'role': '后端开发',
        'question_bank': ROOT / 'companies' / '腾讯' / '微信事业群' / '基础平台' / 'question-bank.md',
        'json_dir': ROOT / 'companies' / '腾讯' / '微信事业群' / '基础平台' / 'interview-experiences',
    },
    {
        'company': '阿里巴巴',
        'business_group': '淘天集团',
        'department': '技术平台',
        'role': '后端开发',
        'question_bank': ROOT / 'companies' / '阿里巴巴' / '淘天集团' / '技术平台' / 'question-bank.md',
        'json_dir': ROOT / 'companies' / '阿里巴巴' / '淘天集团' / '技术平台' / 'interview-experiences',
    },
    {
        'company': '美团',
        'business_group': '到店事业群',
        'department': '后端技术',
        'role': '后端开发',
        'question_bank': ROOT / 'companies' / '美团' / '到店事业群' / '后端技术' / 'question-bank.md',
        'json_dir': ROOT / 'companies' / '美团' / '到店事业群' / '后端技术' / 'interview-experiences',
    },
    {
        'company': '拼多多',
        'business_group': '主站业务',
        'department': '服务端',
        'role': '后端开发',
        'question_bank': ROOT / 'companies' / '拼多多' / '主站业务' / '服务端' / 'question-bank.md',
        'json_dir': ROOT / 'companies' / '拼多多' / '主站业务' / '服务端' / 'interview-experiences',
    },
]

PLACEHOLDERS = ['待补充', '待填写']


def read_state():
    if not STATE_PATH.exists():
        return {}
    return json.loads(STATE_PATH.read_text(encoding='utf-8'))


def write_state(state):
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def is_real_question_bank(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding='utf-8')
    return all(token not in text for token in PLACEHOLDERS) and len(text.strip()) > 200


def json_count(path: Path) -> int:
    if not path.exists():
        return 0
    return len([p for p in path.glob('*.json') if p.name != 'sample.json'])


def build_tasks():
    tasks = []
    for t in TARGETS:
        qb_ok = is_real_question_bank(t['question_bank'])
        jc = json_count(t['json_dir'])
        payload = {
            'company': t['company'],
            'business_group': t['business_group'],
            'department': t['department'],
            'role': t['role'],
        }
        if not qb_ok:
            tasks.append({**payload, 'action': 'fill_question_bank', 'priority': 'P0'})
        if jc == 0:
            tasks.append({**payload, 'action': 'add_interview_json', 'priority': 'P0'})
    return tasks


def summarize(tasks, state):
    done_targets = []
    pending_targets = []
    for t in TARGETS:
        qb_ok = is_real_question_bank(t['question_bank'])
        jc = json_count(t['json_dir'])
        item = {
            'company': t['company'],
            'business_group': t['business_group'],
            'department': t['department'],
            'question_bank_ready': qb_ok,
            'interview_json_count': jc,
        }
        if qb_ok and jc > 0:
            done_targets.append(item)
        else:
            pending_targets.append(item)

    state['generated_at'] = datetime.now(timezone.utc).isoformat()
    state['phase'] = 'collection-and-production'
    state['summary'] = {
        'todo': len(tasks),
        'running': len(state.get('running', [])),
        'completed': len(done_targets),
        'companies_seeded': state.get('summary', {}).get('companies_seeded', 8),
        'question_banks_filled': sum(1 for t in TARGETS if is_real_question_bank(t['question_bank'])),
        'interview_json_count': sum(json_count(t['json_dir']) for t in TARGETS),
    }
    state['next_actions'] = tasks[:6]
    state['completed'] = done_targets
    state['pending'] = pending_targets
    return state


def main():
    state = read_state()
    state.setdefault('running', [])
    state.setdefault('completed', [])
    tasks = build_tasks()
    state = summarize(tasks, state)
    write_state(state)

    print('JobWiki orchestrate summary')
    print(f"phase: {state['phase']}")
    print(f"todo: {state['summary']['todo']}")
    print(f"question_banks_filled: {state['summary']['question_banks_filled']}")
    print(f"interview_json_count: {state['summary']['interview_json_count']}")
    print('next_actions:')
    for item in state['next_actions']:
        print(f"- [{item['priority']}] {item['company']} / {item['business_group']} / {item['department']} / {item['role']} -> {item['action']}")


if __name__ == '__main__':
    main()
