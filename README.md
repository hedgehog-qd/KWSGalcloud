# KWSGalcloud
KWSGalcloud
1.导入数据库

2.导入docker image
	docker load < kwsgalcloud42.tar

3.编辑配置文件config.yaml
(从config_example.yaml作为样板更改)

4.配置启动容器
	端口：内5000 对外 ...
	目录映射：内/docker/config对外 ... (config.yaml所在的位置)
