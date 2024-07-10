#!/bin/bash
set -ex
source ~/miniconda3/etc/profile.d/conda.sh 
conda activate $PWD/.conda
cdeep_jspc_chat \
    --classify-and-rewrite-url="http://192.168.2.187:50021/classify" \
    --rerank-url="http://192.168.2.238:8004/query_bgereranker" \
    --search-url="http://192.168.2.187:8080/search" \
    --final-chat-url="http://192.168.2.187:50021/chat_streaming" \
    --org-chat-model-url="http://qwen32b-gptq.llm.fwqw.cstor.cn/v1/" \
    --org-entity-data-path="mysql+mysqlconnector://root:cstorfs@192.168.2.192:3306/data_center" \
    --host="0.0.0.0" \
    --port=50020