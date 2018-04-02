import xlrd
import xlwt
import types
import xlutils
from xlutils.copy import copy
class AttenceExcel:
    def judge(self,department):
        manager_department = ["安全保卫部","办公室","编辑委员会","播控中心","财务部","产业管理部","党群工作部","覆盖传输中心","工会","广告经营管理中心",
                              "规划建设部","行业社团事务管理中心","湖南广播电视台","监察室","节目交易管理中心","科技管理部","离退休人员管理服务部","人力资源部",
                              "审计部","新闻中心","宣传管理部","战略研发部","制作调度中心","制作调度中心","重点工程建设指挥部","资产管理部","湖南广电系统","金鹰办"]
        satelliteTV_department = ["纪检监察室","北京事业部","刘伟团队","陈汝涵团队","陈歆宇团队","单丹霞团队","导摄部","都艳团队","服装化妆部","覆盖部","规划编排部","后期制作团队",
                                  "节目制作中心","节目资源部","孔晓一团队","李哲团队","梁书源团队","刘建立团队","刘蕾团队","刘庆荣团队","罗强良团队","刘伟团队",
                                  "罗煦明团队","内容服务部","潘瑞芳团队","品牌包装部","品牌管理部","品牌推广部","秦明团队","情报部","沈欣团队","生产资源调度部",
                                  "王琴团队","王恬吴娈团队","吴梦知团队","徐勍团队","许可团队","严典雅团队","演播部","演艺事务部","杨霖团队","余淑君团队","张丹丹陈鹏飞团队",
                                  "制片部","罗旭明团队","综合部","综合事务部","调度部","总编室","规划部","节目部","品牌部","推广部","形象部","行政组","创新研发中心"]
        if department in manager_department:
            return 2
        if department in satelliteTV_department:
            return 1

    def operator(self,filename,SheetNo=0):
        record = xlrd.open_workbook(filename)
        excel = record.sheet_by_index(SheetNo)
        rows = excel.nrows
        cols = excel.ncols
        if excel :
            print('获取excel表成功')
        print(rows,cols)
        start = 0
        while start < rows:
            #留出文件头的行数
            tablerow = 3
            end = start
            table = xlwt.Workbook()
            sheet1 = table.add_sheet('考勤结果')
            while True:
                for coli in range(cols):
                    # 来台天数，不能为字符串。进行对应cell的文件写入
                    if (coli == 4 and type(excel.cell_value(end, coli)) == type(7.0)):
                        #进行从第一个人开始到倒数第二个人的所在组织分类

                        if excel.cell_value(end, coli) <= 7:
                            #pattern = xlwt.Pattern()  # Create the Pattern
                            #pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
                            #pattern.pattern_fore_colour = 2
                            #style = xlwt.XFStyle()  # Create the Pattern
                            #style.pattern = pattern
                            #sheet1.write(tablerow, coli, excel.cell_value(end, coli), style)
                            sheet1.write(tablerow, coli, excel.cell_value(end, coli))
                            # 判断到7天的情况标记
                            #sheet1.write(tablerow, coli + 1, '?')
                            out = excel.cell_value(end, 1)
                            print(out)
                            # sheet1.write(tablerow,coli,excel.cell_value(end,coli),stytle)
                        else:

                            sheet1.write(tablerow, coli, excel.cell_value(end, coli))
                            out = excel.cell_value(end, 1)
                            print(out)
                    else:
                        sheet1.write(tablerow, coli, excel.cell_value(end, coli))
                # 判断是不是到最后一个人了,似乎不用
                """
                if end == rows-1:
                    for coli in range(cols):
                        # 进行最后一个人cell的手工写入
                        if (coli == 3 and type(excel.cell_value(end, coli)) == type(7.0)):
                            if excel.cell_value(end, coli) <= 7:
                                #pattern = xlwt.Pattern()  # Create the Pattern
                                #pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
                                #pattern.pattern_fore_colour = 2
                                #style = xlwt.XFStyle()  # Create the Pattern
                                #style.pattern = pattern
                                #sheet1.write(tablerow, coli, excel.cell_value(end, coli), style)
                                sheet1.write(tablerow, coli, excel.cell_value(end, coli))
                                sheet1.write(tablerow,coli+1,'?')
                                break
                                # sheet1.write(tablerow,coli,excel.cell_value(end,coli),stytle)
                            else:
                                sheet1.write(tablerow, coli, excel.cell_value(end, coli))
                                out = excel.cell_value(end, 0)
                                print(out)
                                break
                """
                # 寻找下一行，while true 循环内
                end = end + 1
                tablerow = tablerow + 1
                #最后一个部门保存，必须在异常出现之前另外处理。
                if end+1>rows:
                    # 文件保存
                    # 设置单元格文字属性
                    style = xlwt.easyxf('font: height 400, , , bold on; align: wrap on, vert centre, horiz center;'"borders: top double, bottom double, left double, right double;")
                    #读取文件所在部门
                    style2 = xlwt.easyxf('align: wrap on, vert centre, horiz center;'"borders: top double, bottom double, left double, right double;")
                    department = excel.cell_value(start, 3)
                    sheet1.write_merge(0, 0, 0, 7, department,style)
                    sheet1.write_merge(1, 1, 0, 3, '2018年01月工作日：22天',style2)
                    sheet1.write_merge(1,1,4,7,'人力资源部2015年02月26日',style2)
                    sheet1.write(2, 0, '员工编号')
                    sheet1.write(2, 1, '姓名')
                    sheet1.write(2, 2, '')
                    sheet1.col(2).width = 4888  # 3333= 1 (one inch)
                    sheet1.write(2, 3,'所在组织')
                    # 设置单元格宽度
                    sheet1.col(3).width = 4888  # 3333= 1 (one inch)
                    sheet1.write(2, 4, '请假天数')
                    sheet1.write(2, 5, '来台天数')
                    #sheet1.write(2, 4, '？表示低于暂定的考勤值')
                    # 异常所属单元格的格宽度
                    #sheet1.col(4).width = 6000
                    sheet1.write(2, 6, '核查后反馈信息')
                    # 设置单元格宽度
                    sheet1.col(6).width = 6666
                    sheet1.write(2,7,'本人签名确认（异常）')
                    sheet1.col(7).width = 4888
                    # 设置人事专员签字位置 tablerow 找到最后一行
                    last = tablerow
                    sheet1.write_merge(last + 1, last + 2, 4, 6, '人事专员签字：')
                    # 设置部门领导专员签字位置
                    last = last + 4
                    sheet1.write_merge(last, last + 2, 4, 6, '部门主任签字：')
                    # 分单位进行进行存储
                    department = excel.cell_value(start, 3)
                    Reasult = self.judge(department)
                    if Reasult == 2:
                        savepath = 'E:\考勤记录分组\总台'
                    else:
                        if Reasult == 1:
                            savepath = 'E:\考勤记录分组\卫视频道'
                        else:
                            savepath = 'E:\考勤记录分组\其他单位'
                    savename = excel.cell_value(end - 1, 3)
                    strsave = savepath + '\\' + savename + '.xls'
                    table.save(strsave)

                #while true 循环终止条件
                if excel.cell_value(end-1, 3) != excel.cell_value(end, 3):
                    break
            #文件保存,正常情况下文件保存过程如下：
            #设置单元格文字属性
            style = xlwt.easyxf('font: height 400, , , bold on; align: wrap on, vert centre, horiz center;'"borders: top double, bottom double, left double, right double;")
            # 读取文件所属部门
            department = excel.cell_value(start, 3)
            sheet1.write_merge(0, 0, 0, 7, department, style)
            sheet1.write_merge(1, 1, 0, 3, '2018年01月工作日：22天')
            sheet1.write_merge(1, 1, 4, 7, '人力资源部2018年02月26日')
            sheet1.write(2, 0, '员工编号')
            sheet1.write(2, 1, '姓名')
            sheet1.write(2, 2, '')
            sheet1.col(2).width = 4888  # 3333= 1 (one inch)
            sheet1.write(2, 3, '所在组织')
            # 设置单元格宽度
            sheet1.col(3).width = 4888  # 3333= 1 (one inch)
            sheet1.write(2, 4, '请假天数')
            sheet1.write(2, 5, '来台天数')
            # sheet1.write(2, 4, '？表示低于暂定的考勤值')
            # 异常所属单元格的格宽度
            # sheet1.col(4).width = 6000
            sheet1.write(2, 6, '核查后反馈信息')
            # 设置单元格宽度
            sheet1.col(6).width = 6666
            sheet1.write(2, 7, '本人签名确认（异常）')
            sheet1.col(7).width = 4888
            # 表格最下方的签字区域
            #设置人事专员签字位置 tablerow 找到最后一行
            last = tablerow
            sheet1.write_merge(last+1,last+2,  4, 6,  '人事专员签字：')
            # 设置部门领导专员签字位置
            last = last +4
            sheet1.write_merge(last ,last+2, 4, 6, '部门主任签字：')
            # 分单位进行进行存储
            Reasult = self.judge(department)
            if   Reasult == 2:
                savepath = 'E:\考勤记录分组\总台'
            else:
                if Reasult == 1:
                    savepath = 'E:\考勤记录分组\卫视频道'
                else:
                    savepath = 'E:\考勤记录分组\其他单位'
            savename = excel.cell_value(end-1,3)
            strsave = savepath+'\\'+savename+'.xls'
            table.save(strsave)
            start = end

OP = AttenceExcel()
OP.operator(r'E:\1月考勤结果（简版）.xlsx')


