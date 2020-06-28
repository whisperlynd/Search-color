<!DOCTYPE html>
<body >
<div id="wc"></div>
<%@ page contentType="text/html; charset=gb2312" %> 
<%@ page language="java" %> 
<%@ page import="com.mysql.jdbc.Driver" %> 
<%@ page import="java.sql.*" %> 
<%@ page import="java.util.ArrayList" %>
<% 
	
						//驱动程序名 
						String driverName="com.mysql.jdbc.Driver"; 
						//数据库用户名 
						String userName="root"; 
						//密码 
						String userPasswd="luoyujia990210"; 
						//数据库名 
						String dbName="eng"; 
						//表名 
						String tableName="cleaned_hm"; 
						//联结字符串 
						String url="jdbc:mysql://localhost/"+dbName+"?user="+userName+"&password="+userPasswd; 
						Class.forName("com.mysql.jdbc.Driver").newInstance(); 
						Connection connection=DriverManager.getConnection(url); 
						Statement statement = connection.createStatement(); 
						int[] count=new int[7];
						int all;
						String []happyt=new String[7];
						
						ArrayList<String> happy = new ArrayList<String>();
						happy.add("achievement");
						happy.add("affection");
						happy.add("enjoy_the_moment");
						happy.add("bonding");
						happy.add("leisure");
						happy.add("nature");
						happy.add("exercise");
						for(int i=0;i<7;i++){
							//int aa=Integer.valueOf('a')+i;
							//char cha = (char) aa;
							//char cha = (char)('a'+i);
							//out.print(happy.get(i));
							//out.print(cha);

							//String sql="SELECT * FROM "+tableName+" where english like 'a%' "+"order by english"; 
							//String sql="SELECT * FROM "+tableName+" where english like '"+cha+"%' "+"order by english"; 
							String sql="SELECT * FROM "+tableName+" where predicted_category = '"+happy.get(i)+"' "; 
							ResultSet rs = statement.executeQuery(sql);  
							// 输出每一个数据值 
							
							String str;
							int j=0;
							while(rs.next()) { 
								//str=(rs.getString(2)).substring(0,1);
								//out.print(str+" "); 
								j++;
							}
							count[i]=j;
							//out.print(" "+j+" <br>"); 
							//out.print(" "+count[i]+" <br>"); 
							rs.close();
						}
						
						 
						statement.close(); 
						connection.close(); 
%>
<script src="d3.v3.min.js"></script>
		<script>
		    var w=window.innerWidth
|| document.documentElement.clientWidth
|| document.body.clientWidth;

			var h=window.innerHeight
|| document.documentElement.clientHeight
|| document.body.clientHeight;
			w=w*0.98;
			h=h*0.95;
			var color=d3.scale.category20();

			
  function getPixelLength(str,fontsize){
    var curLen=0;
    for(var i=0;i<str.length;i++){
      var code=str.charCodeAt(i);
      var pixelLen=code>255?fontsize:fontsize/2;
      curLen+=pixelLen;
    }
    return curLen;
  }

			//var dataset=[100,90,88,700,888,180];
			var dataset=new Array(7);
			<%for (int i=0;i<7;i++){%>
				dataset[<%=i%>]=<%=count[i]%>
			<%}%>
			var ww=w/dataset.length;
			var svg=d3.select("body")
			          .append("svg")
					  .attr("width",w)
					  .attr("height",h);
			var rect=svg.selectAll("rect")
			            .data(dataset)
				        .enter()
			            .append("rect")
                          .attr("x",function(d,i){return w/16+i*w/2/dataset.length})
						  .attr("y",function(d){return h*0.9-d*0.01})
						  .attr("width",ww*0.95/2)
						  .attr("height",function(d){return d*0.01})
						  .attr("fill",function(d,i){return color(i)});
				 
			var rect=svg.selectAll("txt")
			            .data(dataset)
				        .enter()
			            .append("text")
                          .attr("x",function(d,i){return w/16+i*w/2/dataset.length;})
						  .attr("y",function(d){return h*0.9-d*0.01})
                          .text(function(d){return d})
						  .attr("dx",ww/4)
						  .attr("dy","-1em")
						  .attr("text-anchor","middle")
                          .attr("fill",function(d,i){return color(i)});					  
			
			var dataset1=new Array(7);
			
			var word=new Array("成就","爱情","娱乐","人际关系","闲暇","自然","锻炼");

			var dibu=svg.selectAll("txt_db")
			            .data(word)
				        .enter()
			            .append("text")
                          .attr("x",function(d,i){return w/16+i*w/2/dataset.length;})
						  .attr("y",function(d){return h*0.98;})
                          .text(function(d,i){return d;})
						  .attr("dx",ww/4)
						  .attr("dy","-1em")
						  .attr("text-anchor","middle")
                          .attr("fill",function(d,i){return color(i)});	
						  
			var dataset2=new Array("3.png","4.png","5.png","6.png","7.png","8.png","9.png")
						  
			svg.selectAll("img")
		.data(dataset)
		.enter()
		.append("image")
		.attr("width",w/2/dataset.length-20)
		.attr("height",w/2/dataset.length-20)
		.attr("x", function(d, i) {return w/16+i*w/2/dataset.length+5;})
		.attr("y", function(d){return h*0.9-d*0.01-130+5;})
		.attr("xlink:href",function(d,i){return "pic/"+dataset2[i];});
		
		var title1=svg.append("text")
						.attr("x",w/2)
						.attr("y",100)
						.attr("text-anchor","middle")
						.attr("font-size",40)
						.text("What Makes People the Most Happy");
		var title2=svg.append("text")
						.attr("x",w/2)
						.attr("y",150)
						.attr("text-anchor","middle")
						.attr("font-size",30)
						.text("人们因什么而快乐");	
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
						
		

//var dataset=[ ["8000元以上",14.9] , ["5001-8000元",21.4] , ["3001-5000元",32] , ["2001-3000元",10.8] ,
         //   ["1501-2000元",5.3] , ["1001-1500元",2.8] , ["501-1000元",4.4] , ["500元以下",1.5] , ["无收入",7.0] ];

		var pie=d3.layout.pie()
      .value(function(d){
        return d;
      });
var piedata=pie(dataset);

			var pie=d3.layout.pie().value(function(d){return d;});
			var piedata=pie(dataset);
			var innerRadius=75;
			var outerRadius=150;
			var pie1x=350;
			var pie1y=0;
			var pie2x=(w/4)*3+200;
			var pie2y=0;						
			var fontsize=14;
			/*
			var dataset =[{ startAngle:0, endAngle:Math.PI*1.25},
			{ startAngle:Math.PI*1.25, endAngle:Math.PI*1.75},
			{ startAngle:Math.PI*1.75, endAngle:Math.PI*2}
			];
			*/
	
			var arcPath =d3.svg.arc()
							.innerRadius(innerRadius)
							.outerRadius(outerRadius);
			var arcs=svg.selectAll("g")
						.data(piedata)
						.enter()
						.append("g")
						.attr("transform","translate("+((w/2)+pie1x)+","+(h/2+80)+")");
			arcs.append("path")
				.attr("fill",function(d,i){return color(i);})
				.attr("d",function(d){return arcPath(d);});
				
			arcs.append("line")
	.style("stroke","black")
	.each(function(d){
		d.textLine={x1:0,y1:0,x2:0,y2:0};
	})
	.attr("x1",function(d){
		d.textLine.x1=arcPath.centroid(d)[0]*1.5;
		return d.textLine.x1;
	})
	.attr("y1",function(d,i){
		d.textLine.y1=arcPath.centroid(d)[1]*1.5;
		if(i==6)
			return d.textLine.y1-20;
		return d.textLine.y1;
	})
	.attr("x2",function(d){
		// console.log("d.data[0]:  "+d.data[0]);//产商名
		var strLen=getPixelLength("aaassssssa",fontsize)*1;
		var bx=arcPath.centroid(d)[0]*1.5;
		d.textLine.x2=bx>=0?bx+strLen:bx-strLen;
		return d.textLine.x2;
	})
	.attr("y2",function(d,i){
		d.textLine.y2=arcPath.centroid(d)[1]*1.5;
		if(i==6)
			return d.textLine.y2-20;
		return d.textLine.y2;
	});
			/*
			svg.selectAll("path")
				.data(dataset)
				.enter()
				.append("path")
				.attr("d",function(d){return arcPath(d);})
				.attr("transform","translate("+w/2+","+h/2+")")
				.attr("stroke",function(d,i){return color(i);})
				.attr("stroke-width","3px")
				.attr("fill",function(d,i){return color(i);});
				*/

			arcs.append("text")
			.attr("transform", function (d) {
          let x = arcPath.centroid(d)[0] * 1;
          let y = arcPath.centroid(d)[1] * 1;
          return "translate(" + (x) + "," + (y )+ ")";
        })
			.attr("text-anchor","middle")
			.attr("font-size","20px")
			.on("mouseover",function(d,i){
			//if(d.data[1]<10){}
				d3.select(this).attr("font-size",30);
			})
			.on("mouseout",function(d,i){d3.select(this).attr("font-size",20);})
			.attr("fill","white")
			.attr("fill","rgb(0,0,0)")
			.text(function(d){return Math.floor(d.value/1000)+"%";});
		
			arcs.append("text")
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			arcs.append("line")
				.attr("stroke","black")
				.attr("x1",function(d){return arcPath.centroid(d)[0]*(4/3);})
				.attr("y1",function(d,i){return arcPath.centroid(d)[1]*(4/3);})
				.attr("x2",function(d){return arcPath.centroid(d)[0]*1.5;})
				.attr("y2",function(d,i){if(i==6)return arcPath.centroid(d)[1]*1.5-20;return arcPath.centroid(d)[1]*1.5;});
				
			arcs.append("text")
  .attr("transform",function(d,i){
    var x=0;
    var y=0;
    x=(d.textLine.x1+d.textLine.x2)/2;
    y=d.textLine.y1;
    y=y>0?y+fontsize*1.1:y-fontsize*0.4;
	if(i==6){
		return "translate("+x+","+(y-20)+")";
	}
    return "translate("+x+","+y+")";
  }).attr("text-anchor","middle")
				.attr("font-size","20px")
				.attr("fill","rgb(0,0,0)")
				.text(function(d,i){return word[i];});
			//function(d){return d[0];}
			//(function(d){return Math.floor((d.endAngle-d.startAngle)*180/Math.PI)+"°";})
			
			
			
			
			var name=svg.append("text")
						.attr("x",w-w/16)
						.attr("y",h-h/16)
						.attr("text-anchor","middle")
						.attr("font-size",20)
						.text("罗钰佳 程越");
						
						
			var anchor=svg.append("a")
           .attr("href","https://flowingdata.com/2018/06/21/what-makes-people-the-most-happy/")
           .attr("target","_blank");
  //anchor.setAttribute('www.baidu.com','你好呀');
  anchor.append("text")
   .attr("x",w*0.85)
   .attr("y",h-10)
   .text("数据来源：FLOWING DATA");
		</script>

</body>