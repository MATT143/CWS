function showtime() {

            var m_names = ['January', 'February', 'March',
               'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December'];

            var date= new Date();

            var M=m_names[date.getMonth()];
            var D=date.getDate();
            var h= date.getHours();
            var m=date.getMinutes();
            var s=date.getSeconds();
            var session="AM";


            if(h==0) {
                h=12;
            }
            if(h>=12){
                h=h-12;
                session="PM";
            }

             h=(h<10)?"0"+h:h;
             m=(m<10)?"0"+m:m;
             s=(s<10)?"0"+s:s;

            var time= M+"  " +D+"    ,  "+h+":"+m+":"+s+"  "+session
            document.getElementById("datetime").innerText=time;
            document.getElementById("datetime").textContent=time;
            setTimeout(showtime,1000)
        }
        showtime();

function openCity(evt, cityName) {
          var i, tabcontent, tablinks;
          tabcontent = document.getElementsByClassName("tabcontent");
          for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
          }
          tablinks = document.getElementsByClassName("tablinks");
          for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
          }
          document.getElementById(cityName).style.display = "block";
          evt.currentTarget.className += " active";
        }

        // Get the element with id="defaultOpen" and click on it
        document.getElementById("defaultOpen").click();