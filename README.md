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
  <img src="https://cdn.jsdelivr.net/gh/justsong-lab/images/misc/handwriting_generator.png" width="49%" />
  <img src="https://cdn.jsdelivr.net/gh/justsong-lab/images/misc/handwriting_generator_demo2.png" width="49%" /> 
</p>
