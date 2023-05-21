var editor = CodeMirror.fromTextArea(document.getElementById("code-input"), {
  lineNumbers: true,
  mode: "javascript"
});
editor.on("change", function() {
  document.getElementById("code-output").innerHTML = editor.getValue();
});