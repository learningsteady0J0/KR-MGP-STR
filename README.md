# KR-MGP-STR
KR-MGP-STR 프로젝트

## 실행 코드
``` $ CUDA_VISIBLE_DEVICES=2 python3 -m torch.distributed.launch --nproc_per_node=1 --nnodes=1 --master_port 29502 train.py --train_data data/kor_train --valid_data data/kor_eval  --select_data K_ST --batch_ratio 1 --Transformer char-str --TransformerModel=char_str_base_patch4_3_32_128 --imgH 32 --imgW 128 --manualSeed=226 --workers=0 --isrand_aug --scheduler --batch_size=50 --rgb --saved_path ./save --exp_name char_str_kor --valInterval 500 --num_iter 2000000 --lr 1 --character Synthdata_korean_label.pickle ```

## 주요 파일 설명
- train : 모델 학습 파이썬 파일
- test : 모델 평가 파이썬 파일
- utils : 모델에서 사용되는 argument 정리된 파이썬 파일
- create_lmdb_dataset : 학습시 lmdb로 포맷팅된 데이터를 사용한다. 해당 코드는 수집된 이미지와 text파일을 lmdb로 통합시키는 코드
- log_vis : 학습 후 생성된 log파일을 이용해서 loss를 visulization하는 파이썬 파일

#### 데이터는 보안상 올릴 수 없음을 양해해주시면 감사하겠습니다 :)
