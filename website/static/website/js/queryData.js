$(document).ready(()=>{
    let form = $("#query-form-section");
    console.log(form);
    // console.log($("#whatsapp-btn"));
    // console.log($("#email-btn"));
    let obj = {};
    function formDataForWhatsapp(){
        obj.buttonPressed = "whatsapp";
        formData();
    }
    function formDataForEmail(){
        obj.buttonPressed = "email";
        formData();
    }
    function formData(){
        obj.name = $("#query-form-section #name").val();
        obj.email = $("#query-form-section #email").val();
        obj.number = $("#query-form-section #telephone").val();
        obj.startDate = $("#query-form-section #start-date").val();
        obj.endDate = $("#query-form-section #end-date").val();
        obj.pickupPoint = $("#query-form-section #pick-up-point").val();
        obj.dropPoint = $("#query-form-section #drop-point").val();
        obj.totalPassengers = $("#query-form-section #number-of-person").val();
        obj.destination = $("#query-form-section #travel-destination").val();
        obj.vehicleType = $("#query-form-section #vehicle-type").val();
        obj.bikeType = $("#query-form-section #bike-type").val();
        obj.selfType = $("#query-form-section #self-drive-type").val();
        console.log(obj);
        JSON.stringify(obj);
        ajaxCall(obj);
    }

    function ajaxCall(obj){
        
        $.ajax({
            type: "POST",
            url: "", //url need to append
            data: obj,
            contentType: "application/json; charset=utf-8",
            dataType: "JSON",
            success: function(response){
                console.log('data sent successful');
            }
        });
    }


    $("#whatsapp-btn").click(formDataForWhatsapp);
    $("#email-btn").click(formDataForEmail);
})