import argparse
import os
import yaml


def rename_file(dir_config):
    """
    dir_config内のファイル名を変更する

    Args:
        dir_config (dict): 設定情報 (dir_name, prefix, suffix)

    Returns:
        list: 変更後のファイル名リスト
    """
    dir_name = dir_config['dir_name']
    prefix = dir_config['prefix']
    suffix = dir_config['suffix']

    renamed_filenames = []
    for filename in os.listdir(dir_name):
        # ファイル名の分割
        # 拡張子はわけとく
        base_name, ext = os.path.splitext(filename)

        # 新しいファイル名
        new_filename = prefix + base_name + suffix + ext

        # ファイル名の変更
        os.rename(os.path.join(dir_name, filename), os.path.join(dir_name, new_filename))
        renamed_filenames.append(new_filename)

    return renamed_filenames


def rename_files(config_path):
    """
    YAML設定ファイルに基づいて、フォルダ内のファイル名を変更する

    Args:
        config_path (str): 設定ファイルパス

    Returns:
        None
    """
    # 設定ファイル読み込み
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    # フォルダごとにファイル名を変更
    for dir_config in config['target_dirs']:
        renamed_filenames = rename_file(dir_config)
        print(f"{dir_config['dir_name']} のファイル名が {renamed_filenames} に変更されました。")


if __name__ == '__main__':
    # 引数解析
    parser = argparse.ArgumentParser(description='YAML設定ファイルに基づいて、フォルダ内のファイル名を変更するスクリプト')
    parser.add_argument('config_path', type=str, help='設定ファイルパス')

    args = parser.parse_args()

    # ファイル名を変更
    rename_files(args.config_path)
