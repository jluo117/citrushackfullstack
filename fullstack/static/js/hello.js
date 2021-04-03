console.log("Hello World");
$.get( "http://127.0.0.1:8000/getdata", function( data ) {
  console.log(data);
});
$.get("http://127.0.0.1:8000/getrequest",{"val":4,"something":"ACM"},function(data){
  console.log(data);
});
