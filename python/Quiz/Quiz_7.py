def weeklyReportFile_make(week):
    with open("{0}주차.txt".format(week), "w", encoding="utf8") as wRF :
        wRF.write("- {0} 주차 주간보고 -".format(week))
        wRF.write("\n부서 : ")
        wRF.write("\n이름 : ")
        wRF.write("\n업무 요약 : ")
maxWeek = range(1, 51)
for week in maxWeek:
    weeklyReportFile_make(week)
    week += 1


for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file :
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")