﻿# 一级标题
## 二级标题
#### 四级标题  


//////////////////////////////////////////////////////////////////////////  
> 一级引用  
> > 二级引用

//////////////////////////////////////////////////////////////////////////  
空格+空格+回车：表示换行  
一个空行就是新的段落

//////////////////////////////////////////////////////////////////////////  
使用 两个** 或者 __ 包含文字表示粗体。  
**这是粗体字**  
__这也是粗体字__  
 
使用两个* 或者 _ 包含文字表示斜体。  
*斜体字*  
_这也是斜体字_  

使用 三个* 或者 _ 包含文字表示斜体。  
***粗体并斜体***  
//////////////////////////////////////////////////////////////////////////  
链接行内式：
This is [an example](http://example.com/ "Title") inline link, "Title" shown when mouse pointer hovering over the link. 
[This link](http://example.net/) has no title attribute.

链接参考式：
This is [an example][id] reference-style link.
[id]: http://example.com/  "Optional Title Here"
//////////////////////////////////////////////////////////////////////////  
图片行内式  
![Alt text](/path/to/img.jpg)  
![Alt text](/path/to/img.jpg "Optional title")

图片参考式  
![Alt text][id] 「id」是图片参考的名称，图片参考的定义方式则和连结参考一样：  

[id]: url/to/image  "Optional title attribute"
//////////////////////////////////////////////////////////////////////////
表示代码块
```python
**********代码************
**********代码************

```

//////////////////////////////////////////////////////////////////////////  
行内代码`*代码*`

//////////////////////////////////////////////////////////////////////////
有序列表

1. 第一点
2. 第二点
4. 第三点

//////////////////////////////////////////////////////////////////////////
无序列表

+ 呵呵
	* 嘉嘉
	- 嘻嘻
	- 吼吼
		- 嘎嘎
		+ 桀桀  
>     插入块内容   
> 插入内容  
* 哈哈

//////////////////////////////////////////////////////////////////////////  
使用 --- 或者 \*** 或者 * * * 表示水平分割线。

//////////////////////////////////////////////////////////////////////////  
两条竖线就表示表格，至少有三行表格才会出现

|         序号    |    交易名    |    交易说明    |    备注    |
|    ------: |    :-------:    |    :---------   |    ------    |
|    1    |    prfcfg    |    菜单配置    |    可以通过此交易查询到所有交易码和菜单的对应关系    |
|    2    |    gentmo    |    编译所有交易    |    |
|    100000    |    sysdba    |    数据库表模型汇总    |    |

//////////////////////////////////////////////////////////////////////////  
使用 ~~ 表示删除线。
~~删除的内容~~  


要制约的只有一些 HTML 区块元素――比如<div\>、<table\>、<pre\>、<p\> 等标签，必须在前后加上空行与其它内容区隔开，还要求它们的开始标签与结尾标签不能用制表符或空格来缩进。Markdown 的生成器有足够智能，不会在 HTML 区块标签外加上不必要的 <p\> 标签。
</div>

特殊字符自动转换

在 HTML 文件中，有两个字符需要特殊处理： < 和 & 。 < 符号用于起始标签，& 符号则用于标记 HTML 实体，

Markdown 让你可以自然地书写字符，需要转换的由它来处理好了。如果你使用的 & 字符是 HTML 字符实体的一部分，它会保留原状，否则它会被转换成 &amp;。



列表项目可以包含多个段落，每个项目下的段落都必须缩进 4 个空格或是 1 个制表符：

1.  This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.
如果你每行都有缩进，看起来会看好很多，当然，再次地，如果你很懒惰，Markdown 也允许：

*  This is a list item with two paragraphs.

*   Another item in the same list.
如果要在列表项目内放进引用，那 > 就需要缩进：

*   A list item with a blockquote:  
  >     inside a list item.         

如果要放代码区块的话，该区块就需要缩进两次，也就是 8 个空格或是 4 个制表符：

*   一列表项包含一个列表区块：

        <代码写在这>

和程序相关的写作或是标签语言原始码通常会有已经排版好的代码区块，通常这些区块我们并不希望它以一般段落文件的方式去排版，而是照原来的样子显示，Markdown 会用 <pre\> 和 <code\> 标签来把代码区块包起来。


链接辨别标签可以有字母、数字、空白和标点符号，但是并不区分大小写，因此下面两个链接是一样的：

[link text][a]
[link text][A]
隐式链接标记功能让你可以省略指定链接标记，这种情形下，链接标记会视为等同于链接文字，要用隐式链接标记只要在链接文字后面加上一个空的方括号，如果你要让 "Google" 链接到 google.com，你可以简化成：

[Google][]
然后定义链接内容：

[Google]: http://google.com/
