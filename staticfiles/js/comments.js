const commentForm = document.getElementById("commentForm");

// Wrap in if statement so only applied when commentForm exists
if (commentForm) {
    const commentText = commentForm.querySelector("#id_body");
    const reviewIdInput = document.getElementById("form-review-id");
    const submitButton = document.getElementById("submitButton");
    const editButtons = document.getElementsByClassName("btn-edit");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
    for (let button of editButtons) {
      button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment_id");
        const reviewId = button.getAttribute("data-review-id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        let slug = commentForm.getAttribute("data-slug");

        commentText.value = commentContent;
        reviewIdInput.value = reviewId;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `/component/${slug}/edit_comment/${commentId}/`);
        commentForm.scrollIntoView({ behavior: "smooth" });
      });
    }
}
