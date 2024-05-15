import os
import yaml
import argparse


def load_config(config_file):
    """
    YAML形式の設定ファイルを読み込みます。

    Args:
        config_file (str): 設定ファイルのパス。

    Returns:
        dict: 設定ファイルの内容を表す辞書。
    """
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config


def rename_files_in_folder(target_dir):
    """
    フォルダ内のファイルの名前を変更します。

    Args:
        target_dir (dict): 変更対象のフォルダの情報を含む辞書。
            'dir_name': 変更対象のフォルダのパス。
            'prefix': ファイル名の接頭辞として追加される文字列。
            'suffix': ファイル名の接尾辞として追加される文字列。

    Returns:
        list: 変更されたファイル名のリスト。
    """
    dir_name = target_dir['dir_name']
    prefix = target_dir['prefix']
    suffix = target_dir['suffix']
    renamed_files = []

    # フォルダ内のファイルをループして名前を変更
    for filename in os.listdir(dir_name):
        if os.path.isfile(os.path.join(dir_name, filename)):
            new_filename = prefix + filename + suffix
            os.rename(os.path.join(dir_name, filename), os.path.join(dir_name, new_filename))
            renamed_files.append(new_filename)
            print(f"Renamed {filename} to {new_filename} in {dir_name}")

    return renamed_files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename files in folders based on YAML configuration")
    parser.add_argument("config_file", type=str, help="Path to the YAML configuration file")
    args = parser.parse_args()

    config_file = args.config_file
    config = load_config(config_file)

    # 各フォルダに対してファイル名を変更する
    for target_dir in config['target_dirs']:
        rename_files_in_folder(target_dir)
