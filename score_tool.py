#!/usr/bin/env python3
"""实验作业示例代码：简单的成绩统计工具（A 改进版）。"""


def average(scores):
    """计算平均分。"""
    return sum(scores) / len(scores)


def highest(scores):
    """新增：返回最高分。"""
    return max(scores)


def lowest(scores):
    """新增：返回最低分。"""
    return min(scores)


if __name__ == "__main__":
    data = [80, 90, 100]
    print("平均分:", average(data))
    print("最高分:", highest(data))
    print("最低分:", lowest(data))
