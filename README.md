# 手写体生成器
## 用法
```shell script
# 使用 strokes 字体数据
python ./main.py \
--pnt_path ./data/pnt/006 \
--title 标题 \
--content 内容 空格分段

# 使用 ttf 字体数据
python ./main.py \
--ttf_path ./data/ttf/handwriting_font_2.ttf \
--title_scale 0.9 --content_scale 0.7 --spacing_x 7 --spacing_y 20 \
--title 标题 \
--content 内容 空格分段
```

## 演示
<p>
  <img src="https://user-images.githubusercontent.com/39998050/194205271-4f0fd5de-48ff-4bca-9aa8-99ab0e38ed05.png" width="49%" />
  <img src="https://user-images.githubusercontent.com/39998050/194205228-6bdb24af-9b66-4e5a-a811-66c725edac1c.png" width="49%" /> 
</p>
