SCRIPT_PATH=$(dirname "$(realpath -s "$0")")
cd "$SCRIPT_PATH" || exit

cd ..
python3 main.py \
      --project_name transformer_N100_predLong \
      --exp_type pred \
      --data_name N100 \
      --data_type stock \
      --root_path ../../data/ \
      --full_stock_path N100/ \
      --seq_len 60 \
      --label_len 1 \
      --pred_len 1 \
      --enc_in 10 \
      --dec_in 10 \
      --c_out 1 \
      --short_term_len 1 \
      --long_term_len 5 \
      --pred_type label_long_term \
      --d_model 128 \
      --n_heads 4 \
      --e_layers 2 \
      --d_layers 1 \
      --d_ff 256 \
      --dropout 0.05 \
      --rank_alpha 0.5 \
      --train_epochs 60 \
      --itr 1 \
      --batch_size 32 \
      --learning_rate 0.0001 \
      --adjust_interval 10 \
      --num_workers 6 \
      --devices 0 \
