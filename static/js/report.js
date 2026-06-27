const imageInput = document.getElementById("issueImage");
const preview = document.getElementById("previewImage");
const removeBtn = document.getElementById("removeImage");

imageInput.addEventListener("change", function () {

    const file = this.files[0];

    if (!file) return;

    if (!file.type.startsWith("image/")) {

        alert("Please select an image.");

        this.value = "";

        return;

    }

    const reader = new FileReader();

    reader.onload = function (e) {

        preview.src = e.target.result;

        preview.style.display = "block";

        removeBtn.style.display = "inline-block";

    };

    reader.readAsDataURL(file);

});

removeBtn.addEventListener("click", function () {

    imageInput.value = "";

    preview.src = "";

    preview.style.display = "none";

    removeBtn.style.display = "none";

});
