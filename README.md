# 功能
- 采用预训练词向量输出同义词
- 采用预训练词向量及WMD计算文本之间相似性

# 使用
- 下载预训练词向量
    - [Chinese-Word-Vectors
](https://github.com/Embedding/Chinese-Word-Vectors)
    - 将下载的词向量放在data目录下

- http服务提供接口
    ```python
    # host默认0.0.0.0, port默认9004
    python http_server.py --host 0.0.0.0 --port 9004
    ```

- 测试接口
    ```python
    python test_server.py
    ```
