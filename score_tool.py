#!/usr/bin/env python3
"""实验作业示例代码：简单的成绩统计工具。"""


def average(scores):
    """计算平均分。"""
    return sum(scores) / len(scores)


if __name__ == "__main__":
    print(average([80, 90, 100]))
