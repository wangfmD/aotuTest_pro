# -*- coding: utf-8 -*-
class Template_mixin(object):
    """
    Define a HTML template for report customerization and generation.

    Overall structure of an HTML report

    HTML
    +------------------------+
    |<html>                  |
    |  <head>                |
    |                        |
    |   STYLESHEET           |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </head>               |
    |                        |
    |  <body>                |
    |                        |
    |   HEADING              |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   REPORT               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   ENDING               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </body>               |
    |</html>                 |
    +------------------------+
    """
    
    DEFAULT_TITLE = 'Unit Test Report'
    DEFAULT_DESCRIPTION = ''
    HTML_TMPL_CEREPORT = r"""
        <!DOCTYPE html>
        <html>
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                <link rel="stylesheet" href="../assets/css/bootstrap.css" />
                <link rel="stylesheet" href="../assets/css/bootstrap-datetimepicker.css"/>  
                <script type="text/javascript" centerAPI_pro="../assets/js/jquery.min.js"></script>
                 <script type="text/javascript" centerAPI_pro="../assets/js/bootstrap.min.js"></script>
                <script type="text/javascript" centerAPI_pro="../assets/js/bootstrap-datetimepicker.js"></script>
                <script type="text/javascript" centerAPI_pro="../assets/js/bootstrap-datetimepicker.zh-CN.js"></script>

                <title>%(title)s</title>
                <script type="text/javascript">
                    $(document).ready(function(){
                        //文件查询
                        fileText(null);
                        $('#end_date').datetimepicker({
                            format: 'yyyy-mm-dd',
                            language: 'zh-CN',
                            minView: 2,
                            startView: 3,
                            autoclose: true
                        });
                        $("ul>li>a").click(function(){
                            $("#reportFolder").html(this.text+"<span class='caret'></span>")
                        })
                    })
                    function changes(obj){
                            fileText(obj)
                    };
                    //查询方法
                    function fileText(search){
                        var htmlText="";
                        var file=%(file)s
                        for(var i =0 ; i <file.length; i++){
                            var fileName=file[i]
                            if(search==null){
                                if(fileName!="cereport.html"){
                                    htmlText+="<tr>"
                                    htmlText+="<td>"+(i+1)+"</td>"
                                    htmlText+="<td>"+fileName+"</td>"
                                    htmlText+="<td><a href="+fileName+">"+fileName+"</a></td>"
                                    htmlText+="<td>无</td>"
                                    htmlText+="<tr>"
                                    }
                            }else if(search!=null){
                                //截取字符串      0-9  是2016-10-31101031_restult.html  只截取到月
                                var sliceFile=file[i].slice(0,10)
                                console.log(sliceFile)
                                if(search==sliceFile){
                                    if(fileName!="cereport.html"){
                                        htmlText+="<tr>"
                                        htmlText+="<td>"+(i+1)+"</td>"
                                        htmlText+="<td>"+fileName+"</td>"
                                        htmlText+="<td><a href="+fileName+">"+fileName+"</a></td>"
                                        htmlText+="<td>无</td>"
                                        htmlText+="<tr>"
                                        }
                                }
                            }
                        }
                        $("#files").html(htmlText);
                    }
                    //清空按钮
                    function remoteFile(){
                        fileText(null)
                    }
                    
                </script>
                <style>
                    a{ 
                    color:#0044cc;  
                    text-decoration:none; 
                    } 
                </style>
            </head>
            <body>
                <div class="page-header" style="text-align: center">
                    <h1>测试报告详情页面</h1>
                </div>
                <div class="container">
                <input type="text" class="form-control" readonly="" id="end_date" name="end_date" placeholder="请选择结束时间" style="
                    width: 200px;
                    float: right;
                    margin-top: 15px;
                    cursor:pointer;
                    "  onchange = "changes(this.value)">
                <span class="input-group-addon" style="
                    float: right;
                    width: 38px;
                    height: 34px;
                    margin-top: 15px;
                    cursor:pointer;
                " onclick="remoteFile()">
                        <span class="glyphicon glyphicon-remove"></span>
                    </span>
                <table class="table">  
                  <thead>  
                    <tr>  
                      <th>序号</th>  
                      <th>文件名称</th>
                      <th>地址</th>
                      <th>操作</th>
                    </tr>  
                  </thead>  
                  <tbody id="files">  
                    
                  </tbody>  
                </table>  
              </div>
            </body>
        </html>
     """
     
    HTML_TMPL_INDEX = r"""
        <!DOCTYPE html>
        <html>
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                <link rel="stylesheet" href="assets/css/bootstrap.css" />
                <link rel="stylesheet" href="assets/css/bootstrap-datetimepicker.css"/>  
                <script type="text/javascript" centerAPI_pro="assets/js/jquery.min.js"></script>
                 <script type="text/javascript" centerAPI_pro="assets/js/bootstrap.min.js"></script>
                <script type="text/javascript" centerAPI_pro="assets/js/bootstrap-datetimepicker.js"></script>
                <script type="text/javascript" centerAPI_pro="assets/js/bootstrap-datetimepicker.zh-CN.js"></script>
    
                <title>%(title)s</title>
                <script type="text/javascript">
                    $(document).ready(function(){
                        //文件夹查询
                        folderText()
                    })
                    //查询方法
                    function folderText(){
                         var htmlText="";
                        var folder=%(folder)s
                        for(var i =0 ; i <folder.length; i++){
                            var fileName=folder[i]
                            if(fileName!="assets"){
                                htmlText+="<tr>"
                                htmlText+="<td>"+(i+1)+"</td>"
                                htmlText+="<td><a href="+fileName+"/cereport.html>"+fileName+"</a></td>"
                                htmlText+="<tr>"
                                }
                        }
                        $("#files").html(htmlText);
                    }
                </script>
                <style>
                    a{ 
                    color:#0044cc;  
                    text-decoration:none; 
                    } 
                </style>
            </head>
            <body>
                <div class="page-header" style="text-align: center">
                    <h1>所有测试报告管理页面</h1>
                </div>
                <div class="container">
                <table class="table">  
                  <thead>  
                    <tr>  
                      <th>序号</th>  
                      <th>文件夹名称</th>
                    </tr>  
                  </thead>  
                  <tbody id="files">  
                    
                  </tbody>  
                </table>  
              </div>
            </body>
        </html>
     """