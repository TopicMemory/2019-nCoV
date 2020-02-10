import os

def get_cate(data_root):
    for i in sorted(os.listdir(data_root)):
        if i.startswith('.'):
            continue
        yield i, os.path.join(data_root, i)


def get_list(data_root):
    for cate, cate_path in get_cate(data_root):
        yield '## %s' % cate

        for filename in sorted(os.listdir(cate_path)):
            if filename.startswith('.'):
                continue
            if filename.lower().endswith('.jpg') or filename.lower().endswith('.png'):
                yield (
                    '#### %s\n\n'
                    '<img src="%s" width="256">'
                ) % (
                    filename,
                    os.path.join(cate_path, filename)
                )
            else:
                yield '#### %s: <a href="%s"> 播放视频 </a>' % (
                    filename,
                    os.path.join(cate_path, filename)
                )

def main(data_root):
    with open('图片与段子汇总.md', 'w') as f:
        f.write('\n\n'.join([text for text in get_list(data_root)]))


if __name__ == '__main__':
    main('图片视频素材')