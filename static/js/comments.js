
// Edit buttons
const editButtons = document.querySelectorAll(".edit-comment-button");

editButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
        const commentId = button.getAttribute("data-comment-id");
        const reviewId = button.getAttribute("data-review-id");
        const slug = button.getAttribute("data-slug");

        // Select the form for this review
        const form = document.querySelector(`.comment-form[data-slug="${slug}"]`);
        const commentText = form.querySelector(".comment-textarea");
        const reviewIdInput = form.querySelector("input[name='review_id']");
        const submitButton = form.querySelector(".submit-button");

        // Get existing comment content
        const existingText = document.querySelector(`[data-comment-id="${commentId}"]`).innerText;

        // Populate form with existing comment
        commentText.value = existingText;
        reviewIdInput.value = reviewId;
        submitButton.innerText = "Update Comment";

        // Change form action
        form.setAttribute("action", `/component/${slug}/edit_comment/${commentId}/`);

        form.scrollIntoView({ behavior: "smooth" });
    });
});