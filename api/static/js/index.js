function isValidFile(file) {

    file = file.split(".")
    file = file[file.length - 1]
    console.log(file)
    if (file != "zip") {
        return false;
    }
    return true
}

var existFile = false;

function readURL(input) {
    if (input.files && input.files[0]) {

        var reader = new FileReader();

        reader.onload = function (e) {
            $('.image-upload-wrap').hide();

            // $('.file-upload-image').attr('src', e.target.result);
            $('.file-upload-content').show();
            fn = input.files[0].name

            if (!isValidFile(fn)) {
                console.log("invalid!")
                $('.image-title').html("無効な形式！ファイルzipを選択してください");
                $('.image-title').css("color", "#910B0C")
            } else {
                $('.image-title').html(input.files[0].name);
                $('.image-title').css("color", "#2196f3")
                $(".file-upload-btn").css("cursor", "pointer")
                $(".file-upload-btn").css("opacity", 1.0)
                existFile = true
            }

        };

        reader.readAsDataURL(input.files[0]);

    } else {
        removeUpload();
    }
}

function removeUpload() {
    $('.file-upload-input').replaceWith($('.file-upload-input').clone());
    $('.file-upload-content').hide();
    $('.image-upload-wrap').show();
    existFile = false
    $(".file-upload-btn").css("background", "#2196f3")
    $(".file-upload-btn").css("opacity", 0.4)

}

$('.image-upload-wrap').bind('dragover', function () {
    $('.image-upload-wrap').addClass('image-dropping');
});
$('.image-upload-wrap').bind('dragleave', function () {
    $('.image-upload-wrap').removeClass('image-dropping');
});


function upload() {
    console.log("Uploading...")
    var form_data = new FormData();

    if (existFile) {
        form_data.append('file', $('.file-upload-input').prop('files')[0]);
        $("#wait").css("display", "block");
        $(function () {
            $.ajax({
                type: 'POST',
                url: '/uploader',
                data: form_data,
                contentType: false,
                cache: false,
                processData: false,
                success: function (data) {
                    console.log('Success!');
                    $("#wait").css("display", "none");
                    console.log(data)
                    info = data['info']
                    status = info['status']
                    console.log("status: ", status)
                    if (status === "success") {
                        // $("#myModal").modal();
                        // $("#download-final-report").attr("href", "/download/" + data['rd_folder'] );
                        // $("#download-metadata").attr("href", "/download/" + data['rd_folder'] + "/metadata.json");
                        // window.location.replace("/download/" + data['rd_folder']);
                        window.location.replace("/manager/" + data['rd_folder']);
                    } else {
                        console.log("info: ", info)
                        $("#wait").css("display", "none");
                        alert(info['cause'])
                    }


                },
                error: function () {
                    $("#wait").css("display", "none");

                    alert("Something's wrong!")
                }
            })
        });
    }


}
