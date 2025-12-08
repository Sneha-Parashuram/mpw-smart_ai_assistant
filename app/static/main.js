// main.js - UI helpers, dark toggle, small utilities
(function(){
  // Dark mode toggle
  const dt = document.getElementById("darkToggle");
  if(dt){
    const setMode = (dark)=>{
      document.body.classList.toggle("dark", dark);
      localStorage.setItem("dark", dark ? "1" : "0");
    };
    const init = ()=> setMode(localStorage.getItem("dark")==="1");
    init();
    dt.addEventListener("click", ()=>{
      setMode(!(document.body.classList.contains("dark")));
    });
  }

  // Simple toast
  window.toast = function(msg, t=2500){
    let el = document.createElement("div");
    el.textContent = msg;
    el.style.position = "fixed";
    el.style.right = "18px";
    el.style.bottom = "18px";
    el.style.padding = "10px 14px";
    el.style.background = "#111";
    el.style.color = "#fff";
    el.style.borderRadius = "8px";
    el.style.zIndex = 9999;
    el.style.transition = "all .3s";
    document.body.appendChild(el);
    setTimeout(()=> el.style.opacity = "0.92", 10);
    setTimeout(()=> { el.style.opacity = "0"; el.style.transform="translateY(10px)"; }, t);
    setTimeout(()=> el.remove(), t+400);
  };

  // Dashboard rendering helper: expects <canvas id="chartX">
  window.renderLineChart = function(ctx, labels, datasets){
    if(!ctx) return;
    return new Chart(ctx, {
      type: 'line',
      data: {labels: labels, datasets: datasets},
      options:{
        responsive:true,
        maintainAspectRatio:false,
        interaction:{mode:'index',intersect:false},
        plugins:{legend:{display:true}},
        scales:{
          x:{grid:{display:false}},
          y:{beginAtZero:true,grid:{color:'rgba(0,0,0,0.04)'}}
        }
      }
    });
  };

  // small helper to fetch JSON
  window.fetchJson = async function(url, opts){
    const r = await fetch(url, opts);
    try { return await r.json(); }
    catch { return null; }
  };

})();
/* ============= TOP BAR ============== */
.top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 25px;
}

.top-left {
    display: flex;
    align-items: center;
    gap: 10px;
}

.top-profile-pic {
    width: 42px;
    height: 42px;
    border-radius: 50%;
    object-fit: cover;
}

.top-hello {
    font-size: 18px;
    font-weight: 700;
}

.top-right .brand-top {
    font-size: 22px;
    font-weight: 800;
}

/* ============= NAVBAR ============== */

.site-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 25px;
    background: #ffffff;
    border-bottom: 1px solid #eee;
}

.nav-left .nav-profile {
    font-weight: 700;
    color: #000;
}

.nav-menu {
    display: flex;
    gap: 35px; /* pushes items apart */
    margin-left: auto; /* pushes whole menu to right */
}

.nav-menu a {
    text-decoration: none;
    font-weight: 700;
    color: #0f1724;
}

.logout-btn {
    color: #000 !important;
    font-weight: 800 !important;
    margin-left: 30px !important; /* spacing after Dashboard */
}

/* Remove dark mode toggle fully */
.mode-toggle { display: none !important; }
