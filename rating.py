"""从指定的 Codeforces 难度区间随机抽取一道题目。"""

import argparse
import random
import sys
from typing import Any

import requests


API_URL = "https://codeforces.com/api/problemset.problems"


def fetch_problems() -> list[dict[str, Any]]:
    """获取 Codeforces 题库；网络或接口异常时给出友好提示。"""
    try:
        response = requests.get(API_URL, timeout=15)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as exc:
        raise RuntimeError(f"无法访问 Codeforces API：{exc}") from exc
    except ValueError as exc:
        raise RuntimeError("Codeforces API 返回的不是有效 JSON。") from exc

    if data.get("status") != "OK":
        raise RuntimeError(f"Codeforces API 返回错误：{data.get('comment', '未知错误')}")
    return data["result"]["problems"]


def choose_problem(problems: list[dict[str, Any]], low: int, high: int) -> dict[str, Any]:
    """从 [low, high]（闭区间）中随机选择一道有 rating 的题目。"""
    candidates = [
        problem
        for problem in problems
        if isinstance(problem.get("rating"), int)
        and low <= problem["rating"] <= high
        and problem.get("contestId") is not None
        and problem.get("index")
    ]
    if not candidates:
        raise ValueError(f"分数区间 [{low}, {high}] 内没有找到题目。")
    return random.choice(candidates)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="从 Codeforces 指定分数区间随机抽取一道题目。"
    )
    parser.add_argument("low", nargs="?", type=int, help="最低 rating（包含）")
    parser.add_argument("high", nargs="?", type=int, help="最高 rating（包含）")
    args = parser.parse_args()

    if args.low is None:
        args.low = int(input("请输入最低分数（包含）："))
    if args.high is None:
        args.high = int(input("请输入最高分数（包含）："))
    if args.low < 0 or args.high < 0:
        parser.error("分数不能为负数。")
    if args.low > args.high:
        parser.error("最低分数不能高于最高分数。")
    return args


def main() -> int:
    try:
        args = parse_args()
        problem = choose_problem(fetch_problems(), args.low, args.high)
    except (ValueError, RuntimeError, EOFError) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 1

    contest_id = problem["contestId"]
    index = problem["index"]
    url = f"https://codeforces.com/problemset/problem/{contest_id}/{index}"
    print(f"题目：{problem['name']}")
    print(f"分数：{problem['rating']}")
    print(f"链接：{url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
