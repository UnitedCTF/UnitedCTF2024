// I am not part of the challenge, this is just a script to candify the website
window.addEventListener("DOMContentLoaded", function ondomcontentloaded() {
  // Cloudify the fonts
  const style = document.createElement("style");
  style.appendChild(
    document.createTextNode(`
    @font-face {
      font-family: "cloudy";
      src: url("/assets/fonts/cloudy.ttf");
    }

    html {
      font-family: "cloudy" !important;
      color: hsl(300, 100%, 75%); !important;
    }
  `)
  );
  this.document.head.appendChild(style);

  // Add a pink tint
  const tint = this.document.createElement("div");
  Object.assign(tint.style, {
    zIndex: 99999,
    backgroundColor: "rgba(255,105,180,0.4)",
    pointerEvents: "none",
    position: "fixed",
    top: "0px",
    left: "0px",
    width: "100vw",
    height: "100vh",
  });
  this.document.body.appendChild(tint);
});
