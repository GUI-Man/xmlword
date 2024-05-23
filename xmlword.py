from docx import Document
import xlwt
import xlrd
path = 'doc/M3接口分册20240508.docx'

doc = Document(path)
# 输出文件中的所有文字
def extractTitle(paragraph,name):
	if(paragraph.style.name==name):
		return paragraph
	else:
		return None
if __name__ == '__main__':
	title=[]
	second_title=[]
	second_title_content=[]
	first_title_name="附录二级条标题"
	second_level_title_name="附录三级条标题"

	for paragraph in doc.paragraphs:
		# 判断该段落的标题级别
		#print(paragraph.style.name)
		# 这里用isTitle()临时代表，具体见下文介绍的方法
		result=extractTitle(paragraph,first_title_name)
		if(result!=None):
			if(len(title)==0):
				title.append(result.text)
				continue
			title.append(result.text)
			second_title.append(second_title_content)
			second_title_content=[]
		result=extractTitle(paragraph,second_level_title_name)
		if(result!=None):
			second_title_content.append(result.text)
	for i,j in zip(title,second_title):
		print(i)
		for index in j:
			print("\t"+index)
	#读取word文档完成，创建excel表格

	f2=open("result2.xls","w+",encoding='utf-8')
	df2=xlwt.Workbook(f2)
	table2 = df2.add_sheet('test')
	table2.write(0,0,"序号")
	table2.write(0,1,"模块")
	table2.write(0, 2, "用例标题")
	table2.write(0,3,"测试结果")
	line_begin=1
	line_end=1
	for i,j in zip(title,second_title):
		line_end=line_begin+len(j)
		table2.write_merge(line_begin,line_end,1,1,i)
		for index in range(len(j)):
			table2.write(line_begin+index,2,j[index])
		line_begin=line_end+1

	df2.save("./result2.xls")


# 摘要
#
# 二十一世纪，科技的不断发展，移动互联网行业的技术迭代不断深入。
# 电子商务已成为一项较为先进的商业模式在我国快速兴起与发展，网络购物这一行业发展日益成熟，网上购物已成当前购物订单评价方式的主流。
