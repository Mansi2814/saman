var menuItems = document.getElementById("menuItems");
menuItems.style.maxHeight = "0px";

function menutoggle() {
   if (menuItems.style.maxHeight == "0px")
    {
        menuItems.style.maxHeight = "200px"
    }
else {
        menuItems.style.maxHeight = "0px"
    }
}

function togglePopup(product_id){
    console.log(product_id)
    console.log("nhiiii")
    console.log(document.getElementById(product_id))
    document.getElementById(product_id).classList.toggle("active");
}