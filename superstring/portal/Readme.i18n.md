Flask Bable(i18n)
=================

## 安装Flask-Babel

```
pip install flask-babel
```

## 设置Babel

Flask Application目录下创建babel.cfg, 内容如下：

```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

## 生成翻译模版.pot

```
pybabel extract -F babel.cfg -o messages.pot .
```

## 翻译

```
pybabel init -i messages.pot -d translations -l zh_CN
```

该操作会在当前目录下生成translations文件夹，并创建响应的message.po文件

## 编译翻译结果

```
pybabel compile -d translations
```

> 如果无法生成mo文件，请删除.po文件中的 **#fuzzy**

## 更新翻译

```
pybabel update -i messages.pot -d translations
```