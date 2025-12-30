document.addEventListener("DOMContentLoaded", () => {
  const editButtons = document.querySelectorAll(".btn-edit");
  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteConfirm = document.getElementById("deleteConfirm");

  editButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
      event.preventDefault();
      const commentId = button.getAttribute("comment_id");
      if (!commentId) return;

      let path = window.location.pathname;
      // Ensure trailing slash before appending edit path
      if (!path.endsWith("/")) {
        path += "/";
      }
      const editUrl = `${path}edit_comment/${commentId}`;
      window.location.href = editUrl;
    });
  });

  // Wire delete buttons to open modal and set confirm link
  Array.from(deleteButtons).forEach((button) => {
    button.addEventListener("click", (event) => {
      event.preventDefault();
      const commentId = button.getAttribute("comment_id");
      if (!commentId) return;

      let path = window.location.pathname;
      if (!path.endsWith("/")) {
        path += "/";
      }
      const deleteUrl = `${path}delete_comment/${commentId}`;
      deleteConfirm.setAttribute("href", deleteUrl);
      deleteModal.show();
    });
  });
});
