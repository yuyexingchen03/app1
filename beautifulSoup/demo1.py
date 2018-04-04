#!/usr/bin/env python
#coding:utf-8

html_str ="""
<html lang="zh-cn">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Beautiful Soup常见的解析器 - 道高一尺 - 博客园</title>
<link type="text/css" rel="stylesheet" href="/bundles/blog-common.css?v=-hy83QNg62d4qYibixJzxMJkbf1P9fTBlqv7SK5zVL01"/>
<link id="MainCss" type="text/css" rel="stylesheet" href="/skins/coffee/bundle-coffee.css?v=NnZbvdgFaQNhu3t8P4Wsaz98sDQkgRt7Qxq2rzF0ZRU1"/>
<link id="mobile-style" media="only screen and (max-width: 767px)" type="text/css" rel="stylesheet" href="/skins/coffee/bundle-coffee-mobile.css?v=EhLLUe5NHsx18JODVZscd5ef3A8WbJHKTlTvuKQjsl01"/>
<link title="RSS" type="application/rss+xml" rel="alternate" href="http://www.cnblogs.com/themost/rss"/>
<link title="RSD" type="application/rsd+xml" rel="EditURI" href="http://www.cnblogs.com/themost/rsd.xml"/>
<link type="application/wlwmanifest+xml" rel="wlwmanifest" href="http://www.cnblogs.com/themost/wlwmanifest.xml"/>
<script src="//common.cnblogs.com/scripts/jquery-2.2.0.min.js"></script>
<script type="text/javascript">var currentBlogApp = 'themost', cb_enable_mathjax=false;var isLogined=false;</script>
<script src="/bundles/blog-common.js?v=taItysi72HxMPeH9Xg5nAYabRul6hhgahi3tVIMIKV81" type="text/javascript"></script>
</head>
<body>
<a name="top"></a>

<!--done-->
<div id="home">
<div id="header">
	<div id="blogTitle">
	<a id="lnkBlogLogo" href="http://www.cnblogs.com/themost/"><img id="blogLogo" src="/Skins/custom/images/logo.gif" alt="返回主页" /></a>			
		
<!--done-->
<h1><a id="Header1_HeaderTitle" class="headermaintitle" href="http://www.cnblogs.com/themost/">道高一尺</a></h1>
<h2></h2>



		
	</div><!--end: blogTitle 博客的标题和副标题 -->
</div><!--end: header 头部 -->

<div id="main">
	<div id="mainContent">
	<div class="forFlow">
		<div id="navigator">
			
<ul id="navList">
	<li><a id="blog_nav_sitehome" class="menu" href="http://www.cnblogs.com/">博客园</a></li>
	<li><a id="blog_nav_myhome" class="menu" href="http://www.cnblogs.com/themost/">首页</a></li>
	<li><a id="blog_nav_newpost" class="menu" rel="nofollow" href="https://i.cnblogs.com/EditPosts.aspx?opt=1">新随笔</a></li>
	<li><a id="blog_nav_contact" accesskey="9" class="menu" rel="nofollow" href="https://msg.cnblogs.com/send/%E9%81%93%E9%AB%98%E4%B8%80%E5%B0%BA">联系</a></li>
	<li><a id="blog_nav_admin" class="menu" rel="nofollow" href="https://i.cnblogs.com/">管理</a></li>
	<li><a id="blog_nav_rss" class="menu" href="http://www.cnblogs.com/themost/rss">订阅</a>
	<a id="blog_nav_rss_image" class="aHeaderXML" href="http://www.cnblogs.com/themost/rss"><img src="//www.cnblogs.com/images/xml.gif" alt="订阅" /></a></li>
</ul>


			<div class="blogStats">
				
				<div id="blog_stats">
<!--done-->
随笔- 405&nbsp;
文章- 11&nbsp;
评论- 4&nbsp;
</div>
				
			</div><!--end: blogStats -->
		</div><!--end: navigator 博客导航栏 -->
		
<div id="post_detail">
<!--done-->
<div id="topics">
	<div class = "post">
		<h1 class = "postTitle">
			<a id="cb_post_title_url" class="postTitle2" href="http://www.cnblogs.com/themost/p/7223907.html">Beautiful Soup常见的解析器</a>
		</h1>
		<div class="clear"></div>
		<div class="postBody">
			<div id="cnblogs_post_body" class="blogpost-body"><p>Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器，如果我们不安装它，则 Python 会使用 Python默认的解析器，lxml 解析器更加强大，速度更快，推荐安装。</p>
<div>
<p>&nbsp;</p>
<table>
<tbody>
<tr><th class="head">解析器</th><th class="head">使用方法</th><th class="head">优势</th><th class="head">劣势</th></tr>
</tbody>
<tbody valign="top">
<tr>
<td>Python标准库</td>
<td>BeautifulSoup(markup, “html.parser”)</td>
<td>
<ul class="first last simple">
<li>Python的内置标准库</li>
<li>执行速度适中</li>
<li>文档容错能力强</li>
</ul>
</td>
<td>
<ul class="first last simple">
<li>Python 2.7.3 or 3.2.2)前 的版本中文档容错能力差</li>
</ul>
</td>
</tr>
<tr>
<td>lxml HTML 解析器</td>
<td>BeautifulSoup(markup, “lxml”)</td>
<td>
<ul class="first last simple">
<li>速度快</li>
<li>文档容错能力强</li>
</ul>
</td>
<td>
<ul class="first last simple">
<li>需要安装C语言库</li>
</ul>
</td>
</tr>
<tr>
<td>lxml XML 解析器</td>
<td>BeautifulSoup(markup, [“lxml”, “xml”])BeautifulSoup(markup, “xml”)</td>
<td>
<ul class="first last simple">
<li>速度快</li>
<li>唯一支持XML的解析器</li>
</ul>
</td>
<td>
<ul class="first last simple">
<li>需要安装C语言库</li>
</ul>
</td>
</tr>
<tr>
<td>html5lib</td>
<td>BeautifulSoup(markup, “html5lib”)</td>
<td>
<ul class="first last simple">
<li>最好的容错性</li>
<li>以浏览器的方式解析文档</li>
<li>生成HTML5格式的文档</li>
</ul>
</td>
<td>
<ul class="first last simple">
<li>速度慢</li>
<li></li>
</ul>
</td>
</tr>
</tbody>
</table>
</div></div><div id="MySignature"></div>
<div class="clear"></div>
<div id="blog_post_info_block">
<div id="BlogPostCategory"></div>
<div id="EntryTag"></div>
<div id="blog_post_info">
</div>
<div class="clear"></div>
<div id="post_next_prev"></div>
</div>


		</div>
		<div class = "postDesc">posted @ <span id="post-date">2017-07-23 10:36</span> <a href='http://www.cnblogs.com/themost/'>道高一尺</a> 阅读(<span id="post_view_count">...</span>) 评论(<span id="post_comment_count">...</span>)  <a href ="https://i.cnblogs.com/EditPosts.aspx?postid=7223907" rel="nofollow">编辑</a> <a href="#" onclick="AddToWz(7223907);return false;">收藏</a></div>
	</div>
	<script type="text/javascript">var allowComments=true,cb_blogId=329646,cb_entryId=7223907,cb_blogApp=currentBlogApp,cb_blogUserGuid='be37aac3-3ae2-e611-845c-ac853d9f53ac',cb_entryCreatedDate='2017/7/23 10:36:00';loadViewCount(cb_entryId);var cb_postType=1;</script>
	
</div><!--end: topics 文章、评论容器-->
</div><a name="!comments"></a><div id="blog-comments-placeholder"></div><script type="text/javascript">var commentManager = new blogCommentManager();commentManager.renderComments(0);</script>
<div id='comment_form' class='commentform'>
<a name='commentform'></a>
<div id='divCommentShow'></div>
<div id='comment_nav'><span id='span_refresh_tips'></span><a href='javascript:void(0);' onclick='return RefreshCommentList();' id='lnk_RefreshComments' runat='server' clientidmode='Static'>刷新评论</a><a href='#' onclick='return RefreshPage();'>刷新页面</a><a href='#top'>返回顶部</a></div>
<div id='comment_form_container'></div>
<div class='ad_text_commentbox' id='ad_text_under_commentbox'></div>
<div id='ad_t2'></div>
<div id='opt_under_post'></div>
<div id='cnblogs_c1' class='c_ad_block'></div>
<div id='under_post_news'></div>
<div id='cnblogs_c2' class='c_ad_block'></div>
<div id='under_post_kb'></div>
<div id='HistoryToday' class='c_ad_block'></div>
<script type='text/javascript'>
    fixPostBody();
    setTimeout(function () { incrementViewCount(cb_entryId); }, 50);
    deliverAdT2();
    deliverAdC1();
    deliverAdC2();    
    loadNewsAndKb();
    loadBlogSignature();
    LoadPostInfoBlock(cb_blogId, cb_entryId, cb_blogApp, cb_blogUserGuid);
    GetPrevNextPost(cb_entryId, cb_blogId, cb_entryCreatedDate, cb_postType);
    loadOptUnderPost();
    GetHistoryToday(cb_blogId, cb_blogApp, cb_entryCreatedDate);   
</script>
</div>


	</div><!--end: forFlow -->
	</div><!--end: mainContent 主体内容容器-->

	<div id="sideBar">
		<div id="sideBarMain">
			
<!--done-->
<div class="newsItem">
<h3 class="catListTitle">公告</h3>
	<div id="blog-news"></div><script type="text/javascript">loadBlogNews();</script>
</div>

			<div id="calendar"><div id="blog-calendar" style="display:none"></div><script type="text/javascript">loadBlogDefaultCalendar();</script></div>
			
			<DIV id="leftcontentcontainer">
				<div id="blog-sidecolumn"></div><script type="text/javascript">loadBlogSideColumn();</script>
			</DIV>
			
		</div><!--end: sideBarMain -->
	</div><!--end: sideBar 侧边栏容器 -->
	<div class="clear"></div>
	</div><!--end: main -->
	<div class="clear"></div>
	<div id="footer">
		
<!--done-->
Copyright &copy;2018 道高一尺
	</div><!--end: footer -->
</div><!--end: home 自定义的最大容器 -->
</body>
</html>
"""


from bs4 import BeautifulSoup
import codecs
'''
可以通过字符串的方式创构建BeautifulSoup对象
    也可以通过文件来构建BeautifulSoup对象
    from_encoding='utf-8' 这个可以省略 默认就是utf-8编码
'''
soup =BeautifulSoup(html_str,'lxml',from_encoding='utf-8')
al = soup.find_all('a')
for a in al:
    print("href:",a.get('href'))

soup =BeautifulSoup(codecs.open('index.html','r',encoding='UTF-8'),'lxml')
al = soup.find_all('a')
for a in al:
    print("href:",a.get('href'))

'''
    格式化输出html
'''
print(soup.prettify())

'''
    Tag
    抽取标签元素
        这种方式只能获取第一个
'''
print("Tag------>",soup.a)

'''
    Tag
        可以获取属性.也可以修改属性
        还有个特殊性的属性name为获取当前tag的名称
'''
print(soup.a.href)
soup.a.href = '修改后的属性'
print(soup.a.href)
print(soup.a.name)
print(soup.name)

'''
    Tag标签之间的内容(NavigableString)
        string(不能含有子Tag,否则不起作用)
'''
print(soup.p.string)
print(soup.title.string)