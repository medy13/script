exportData脚本使用说明
====================
*	oracle环境配置

		sftp root@10.3.50.249:/home/oracle_min_client_11.2.0.tar.gz .
		vim oracle.profile　//修改ORACLE_BASE的地址
		source oracle.profile

*	脚本说明

|名称	|说明	|
|-------|-------|
|`oracle.profile`	|oralce运行环境配置文件|
|`export_bushuji.sh`	|补历史数据的脚本,使用`export_bushuji.sh　<args0>` 参数格式:yyyymmddhhmiss
|`nextDate_exec_980.sh`	|数据导出脚本与`export_bushuji.sh`结合使用
|`runDayAll.sh`	|手动导出一天的数据,与`export_bushuji.sh`和`nextDate_exec_980.sh`结合使用
|`curt_exportData.sh`	|导出当前数据,每三个小时自动运行一次,导出这三个小时内产生的数据