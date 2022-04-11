let optionList = document.createElement("select");
var arr = JSON.parse(sessionStorage.getItem("ALL"));
// document.querySelector("#result").innerHTML = arr;
var btn = document.createElement("BUTTON");
var count = 0;
//var data = {};
btn.innerHTML = "New Button";

// 課堂數
var classesnumber = {};

// 老師志願序
var jsonObj = [];

// console.log(typeof arr);
// console.log(arr);

for(var i = 0; i < arr.length; i++) 
{
    var opt = document.createElement('option');
    opt.innerHTML = arr[i];
    opt.value = arr[i];
    optionList.appendChild(opt);
}

var classes = document.createElement('div');
for(var i =0; i < arr.length; i++)
{
    newList = optionList.cloneNode(true);
    newList.setAttribute("class", i);
    newList.setAttribute("id", null);
    classes.innerHTML += newList.outerHTML;
    classes.innerHTML = classes.innerHTML + "<input type='text' class='" + i +"'><br>";
}
document.getElementById("numbers").appendChild(classes);


document.getElementById("addteacher").addEventListener("click",()=>{createNewElement()}, false);
function createNewElement() {
    count += 1;

    // First create a DIV element.
    var txtNewInputBox = document.createElement('div');

    // Then add the content (a new input box) of the element.
    txtNewInputBox.innerHTML = "老師"+ count +"<input type='text' id='name'"+'class = teacher'+ count + ">年資<input type='text' id='stayage'"+'class = teacher'+ count + ">年齡<input type='text' id='age'"+'class = teacher'+ count + "><br>";


    for(var i = 0; i < arr.length; i++){
        optionList.setAttribute("id", "priority" + (i+1));
        optionList.setAttribute("class", "teacher" + count);
        txtNewInputBox.innerHTML += ("志願" + (i+1) + optionList.outerHTML);
    }

    txtNewInputBox.setAttribute("id", "teacher" + count);
    txtNewInputBox.setAttribute("class", "teacher" + count);
    //console.log(txtNewInputBox.outerHTML);
    txtNewInputBox.innerHTML = txtNewInputBox.innerHTML + "<br>";

    // Finally put it where it is supposed to appear.
    document.getElementById("newElementId").appendChild(txtNewInputBox);
}

document.getElementById("btn-submit").addEventListener("click",()=>{submit()}, false);
eel.expose(submit);
function submit() {
    teacher = [];
    for(var i = 0; i < count; i++){
        teacher[i+1] = 'teacher' + (i+1);
        console.log(teacher[i+1]);
    }
    nums = [];
    for(var i = 0; i < arr.length; i++){
        $("div[id=numbers]").each(function(){
            var tempclass = document.getElementsByClassName(i);
            console.log(tempclass);
            temp = {};
            temp[tempclass[0].value] = tempclass[1].value;
            nums.push(temp);
        })
    }
    console.log(nums);
    
    for(var i = 0; i < count; i++)
    {
        temp = [];
        stringteacher = 'teacher' + (i+1);
        $("div[class=teacher"+ (i+1) + "]").each(function() {
    
    
            teacher[i+1] = {};
            teacher[i+1]["name"] = document.getElementById("teacher"+(i+1)).querySelector("#name").value;
            teacher[i+1]["stayage"] = document.getElementById("teacher"+(i+1)).querySelector("#stayage").value;
            teacher[i+1]["age"] = document.getElementById("teacher"+(i+1)).querySelector("#age").value;
            for(var j = 0; j < arr.length; j++){
                temp.push(document.getElementById("teacher"+(i+1)).querySelector("#priority" + (j+1)).value);
                //console.log("teacher:"+ (i+1) + ", " + "priority"+ (j+1) + ":" + document.getElementById("teacher"+(i+1)).querySelector("#priority" + (j+1)).value);
            }
            teacher[i+1]["priority"] = temp;        
        });
        jsonObj.push(teacher[i+1]);
    }

    sessionStorage.setItem("classnums", JSON.stringify(nums));
    sessionStorage.setItem("result", JSON.stringify(jsonObj));
    // console.log(nums);
    // console.log(jsonObj);
    window.location.href = "result.html";
}


// 分發
function test(){
    var result = JSON.parse(sessionStorage.getItem("result"));
    var classnums = JSON.parse(sessionStorage.getItem("classnums"));
    // console.log(result);
    // console.log(classnums);
    
    var Teacherpriority = []
    for(var i = 0; i < result.length;i++){
        Teacherpriority[i] = {};
        Teacherpriority[i]['name'] = result[i]['name'];
        Teacherpriority[i]['total'] = result[i]['age'] * 0.5 + result[i]['stayage'] * 0.5;
        Teacherpriority[i]['priority'] = result[i]['priority'];
        Teacherpriority[i]["total"] = 0;
        // console.log("result[i]['age']:"+result[i]['age']);
        // console.log("result[i]['stayage']:"+result[i]['stayage']);
        // console.log("Teacherpriority[result[i]['name']]:"+Teacherpriority[result[i]['name']]);
    }
    Teacherpriority.sort(function(a, b){
        console.log("正");
        return b.total - a.total;
    });

    //document.getElementById("test").innerHTML = JSON.stringify(Teacherpriority);

    resultteacher = []
    tempforclass = {}

    var UNFinished = true;
    var ALLnull = false;
    iCount = 0;


    while(true){
        iCount += 1;
        console.log("第"+iCount+"輪");
        //console.log(Teacherpriority);
        //console.log(classnums);


        // 檢查堂數是否歸0
        UNFinished = false;
        classnums.forEach(e =>{
            //console.log(e);
            for(var key in e){
                if(e.hasOwnProperty(key)){
                    if(!(e[key] == 0)){
                        UNFinished = true;
                    }
                }
            }
        });
        if(!UNFinished){
            break;
        }

        // 檢查是否所有老師都分發完畢
        ALLnull = true;
        Teacherpriority.forEach( e => {
            if (!(e['priority'].length == 0)){
                ALLnull = false;
                // console.log(e['priority'].length);
                console.log(e["total"]);
            }
        });
        if(ALLnull){
            break;
        }

        
        for(var i = 0; i < Teacherpriority.length; i++)
        {
            console.log(Teacherpriority[i]["name"]);
            console.log(Teacherpriority[i]['priority']);
            console.log(Teacherpriority[i]["total"]);

            if(Teacherpriority[i]["total"] < 2){
                for(var j = 0; j < Teacherpriority[i]['priority'].length; j++){
                    console.log(Teacherpriority[i]['priority'][j]);
                    // console.log(classnums[j]);
                    // console.log(classnums[j][Teacherpriority[i]['priority'][j]]);

            hasclass = true;
            for(var z = 0; z < classnums.length; z++){
                if(classnums[z].hasOwnProperty(Teacherpriority[i]['priority'][j])){
                    console.log(classnums[z][Teacherpriority[i]['priority'][j]]);
                    if(classnums[z][Teacherpriority[i]['priority'][j]] > 0){
                        classnums[z][Teacherpriority[i]['priority'][j]] -= 1;
                    }else{
                        console.log("break");
                        hasclass = false;                        
                    }
                }
            }

            if(!hasclass){
                continue;
            }
                    // if(classnums[j].hasOwnProperty(Teacherpriority[i]['priority'][j])){                    
                    //     if(classnums[j][Teacherpriority[i]['priority'][j]] > 0){
                    //         classnums[j][Teacherpriority[i]['priority'][j]] -= 1;
                    //     }else{
                    //         console.log("break");
                    //         continue;
                    //     }
                    // }
                    // console.log(classnums);
                    //console.log(JSON.stringify(classnums[j]) + ":" + classnums[j][Teacherpriority[i]['priority'][j]]);
                    // console.log(Teacherpriority[i]['name']);
                    tempforclass[Teacherpriority[i]['priority'][j]] += Teacherpriority[i]['name'] + ',';
                    tempforclass[Teacherpriority[i]['priority'][j]] = tempforclass[Teacherpriority[i]['priority'][j]].replace('undefined', '');
                    
                    // console.log(tempforclass);

                    //resultteacher[Teacherpriority[i]['priority'][j]] = tempforclass;

                    Teacherpriority[i]["total"] += 1;
                    var index = Teacherpriority[i]['priority'].indexOf(Teacherpriority[i]['priority'][j]);
                    console.log(index);           
                    if (index !== -1) {
                        Teacherpriority[i]['priority'].splice(index, 1);               
                    }
                    break;

                    //console.log(classnums);
                }
                //resultteacher.push(tempforclass);
                //console.log(resultteacher);
            }else{
                Teacherpriority[i]["priority"] = [];
            };

        }

        // if((iCount % 2) == 0){
        //     Teacherpriority.sort(function(a, b){
        //         console.log("正");
        //         return b.total - a.total;          
        //     });
        // }else{
        //     Teacherpriority.sort(function(a, b){
        //         console.log("反");              
        //         return a.total - b.total;
        //     });

        // }
        Teacherpriority.reverse();

    }

    var resultclass = [];
    console.log(Object.keys(tempforclass));
    Object.keys(tempforclass).forEach(e =>{
        resultclass.push(e);
    });

    resultclass.forEach(e =>{
        console.log(e);
        counter = 0;
        tempstr = "";
        for (var i = 0; i < e.length; i++) {
            if(e[i] == ','){
                continue;
            }
            if(e[i] != ','){
                counter++;               
                tempstr += e[i];
                console.log(tempstr);
            }
            if(counter % 4 == 0){
                console.log(tempstr);
                document.getElementById(tempstr).innerHTML = tempforclass[e];
                tempstr = "";
                console.log(tempforclass[e]);
                console.log(counter);
            }
          }
    });

}