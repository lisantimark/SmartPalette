
    //Initiates preview of palette with options
    $('#generateButton').click(function (evt) {
        evt.preventDefault();
        //Get selected palette input
        var color_number = $('#paletteNumberSelect').val();
        var palette_width = ($('.main-content .container').width()) / color_number;
        var palette_height = (50);
        //Create new divs to add

        var color_placeholders = ("<div class='palette-block'></div>");
        //Remove contents then add appropriate amount of new palette blocks
        for (i = 0; i < color_number; i++) {
            $('.main-content .container').fadeIn(1500).append(color_placeholders);
        }
        //Add loop to assign generated colors to display
        //Red assigned for testing
        $('.palette-block').each(function () {
            $(this).css('background-color', 'red');
        })
        $('.palette-block').css('width', palette_width).css('height', palette_height);
    });

//Loads image to display
//Need to store image data
function readFile() {
    var reader = new FileReader();
    reader.onload = function () {
        var output = document.getElementById('output');
        output.src = reader.result;
    };
    reader.readAsDataURL(event.target.files[0])
};



