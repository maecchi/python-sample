#!/usr/bin/env python

import subprocess
import sys


def execClassification():
    """
    画像分類を実行し、分類結果を返却する

    Returns
    ----------
    cmd : string
        画像分類スクリプト出力結果文字列

    Notes
    ----------
    コマンド引数の情報に不備があった場合はコメントを出力して終了する
    """

    # 引数に画像ファイル名を受け取り画像分類にかける
    args = sys.argv

    if len(args) == 1:
        print("引数にファイルパスを入力してください")
        sys.exit(0)
    filepath = args[1]

    check_cmd = "file " + filepath
    check_output = subprocess.check_output(check_cmd.split())
    check_msg = 'No such file or directory'

    if check_msg in str(check_output):
        print("指定されたファイルパスにファイルは存在しません")
        sys.exit(0)

    cmd = "python label_image.py --image " + filepath + \
        " --graph retrained_graph.pb --labels retrained_labels.txt --input_layer=Placeholder"

    # 実行結果の数値を読み取り、分類判定結果（どのカテゴリに属するか）を出力したい
    cmd_result = subprocess.check_output(cmd.split(), universal_newlines=True)

    return cmd_result


def identifiedClass(cmd_result):
    """
    引数の分類結果を解析し、分類結果を返却する

    Parameters
    ----------
    cmd_result : string
        画像分類実行結果出力文字列

    Returns
    ----------
    class_name : string
        画像分類判定結果
    """
    line_list = cmd_result.splitlines()

    result_list = {}
    for line in line_list:
        tmp = line.split(' ')
        result_list[tmp[0]] = float(tmp[1])

    # max(k, key=k.get)
    ## key: 辞書kのkeyの各要素に対して比較前に実行される処理
    # よってmaxで比較される要素はk.get()により取得した要素群になる
    class_name = max(result_list, key=result_list.get)

    return class_name


def output(class_name, cmd_result):
    """
    出力関数
    """
    print("分類結果: %s" % class_name)
    print("---- 判定詳細 ----")
    print(cmd_result)


def main():
    """
    main関数
    """
    cmd_result = execClassification()
    class_name = identifiedClass(cmd_result)
    output(class_name, cmd_result)


if __name__ == "__main__":
    main()
