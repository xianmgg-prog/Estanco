<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <title>Estanco Analytics Dashboard</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <!-- Estilos básicos profesionales -->
  <style>
    body {
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      margin: 0;
      background-color: #0f172a;
      color: #e5e7eb;
    }
    header {
      padding: 1.5rem 2rem;
      border-bottom: 1px solid #1f2937;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: linear-gradient(90deg, #0f172a, #111827);
    }
    header h1 {
      margin: 0;
      font-size: 1.5rem;
    }
    main {
      padding: 1.5rem 2rem;
      max-width: 1200px;
      margin: 0 auto;
    }
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 1rem;
      margin-bottom: 1.5rem;
    }
    .card {
      background-color: #111827;
      border: 1px solid #1f2937;
      border-radius: 0.75rem;
      padding: 1rem;
    }
    .card h2 {
      margin: 0 0 0.5rem 0;
      font-size: 1rem;
      color: #9ca3af;
    }
    .metric {
      font-size: 1.4rem;
      font-weight: 600;
    }
    .tabs {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 1rem;
    }
    .tab-button {
      padding: 0.5rem 1rem;
      border-radius: 999px;
      border: 1px solid #1f2937;
      background-color: #111827;
      color: #e5e7eb;
      cursor: pointer;
      font-size: 0.9rem;
    }
    .tab-button.active {
      background-color: #2563eb;
      border-color: #2563eb;
    }
    .section {
      margin-bottom: 1.5rem;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
    }
    th, td {
      padding: 0.5rem;
      border-bottom: 1px solid #1f2937;
    }
    th {
      text-align: left;
      background-color: #030712;
      color: #9ca3af;
    }
    tr:nth-child(even) {
      background-color: #020617;
    }
    select, input[type="file"] {
      background-color: #020617;
      color: #e5e7eb;
      border: 1px solid #1f2937;
      border-radius: 999px;
      padding: 0.4rem 0.8rem;
      font-size: 0.85rem;
    }
    .controls {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      margin-bottom: 1rem;
      align-items: center;
    }
    canvas {
      width: 100%;
      max-height: 300px;
    }
    .badge {
      display: inline-block;
      padding: 0.15rem 0.5rem;
      border-radius: 999px;
      background-color: #1f2937;
      font-size: 0.75rem;
      color: #9ca3af;
    }
  </style>
  <!-- Chart.js para gráficos -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
  <header>
    <h1>🚬 Estanco Analytics Dashboard</h1>
    <div>
      <input type="file" id="fileInput" accept=".csv" />
      <span class="badge">Sube tu CSV de ventas</span>
    </div>
  </header>
  <main>
    <!-- KPIs -->
    <section class="grid-3">
      <div class="card">
        <h2>Ingresos totales</h2>
        <div id="kpiIngresos" class="metric">– €</div>
      </div>
      <div class="card">
        <h2>Beneficio estimado</h2>
        <div id="kpiBeneficio" class="metric">– €</div>
      </div>
      <div class="card">
        <h2>Rotación media</h2>
        <div id="kpiRotacion" class="metric">– veces</div>
      </div>
    </section>

    <!-- Tabs -->
    <section class="section">
      <div class="tabs">
        <button class="tab-button active" data-tab="resumen">Resumen</button>
        <button class="tab-button" data-tab="productos">Productos</button>
        <button class="tab-button" data-tab="categorias">Categorías</button>
        <button class="tab-button" data-tab="graficos">Gráficos</button>
      </div>
    </section>

    <!-- Contenido de tabs -->
    <section id="tabResumen" class="section">
      <div class="card">
        <h2>Datos de ventas (tabla)</h2>
        <div id="tablaResumen"></div>
      </div>
    </section>

    <section id="tabProductos" class="section" style="display:none">
      <div class="card">
        <h2>Ranking de productos</h2>
        <div class="controls">
          <label>Métrica:
            <select id="rankingMetric">
              <option value="unidades_vendidas">Unidades vendidas</option>
              <option value="ingresos">Ingresos</option>
              <option value="beneficio">Beneficio</option>
              <option value="rotacion">Rotación</option>
            </select>
          </label>
          <label>Top N:
            <select id="rankingTop">
              <option value="5">5</option>
              <option value="10" selected>10</option>
              <option value="15">15</option>
              <option value="20">20</option>
            </select>
          </label>
        </div>
        <div id="tablaProductos"></div>
      </div>
    </section>

    <section id="tabCategorias" class="section" style="display:none">
      <div class="card">
        <h2>Resumen por categoría</h2>
        <div id="tablaCategorias"></div>
      </div>
    </section>

    <section id="tabGraficos" class="section" style="display:none">
      <div class="card">
        <h2>Gráfico por categoría</h2>
        <div class="controls">
          <label>Métrica:
            <select id="grafCategoriaMetric">
              <option value="ingresos_total">Ingresos</option>
              <option value="beneficio_total">Beneficio</option>
              <option value="unidades_total">Unidades</option>
            </select>
          </label>
        </div>
        <canvas id="chartCategorias"></canvas>
      </div>

      <div class="card" style="margin-top:1rem">
        <h2>Gráfico de productos</h2>
        <div class="controls">
          <label>Métrica:
            <select id="grafProductosMetric">
              <option value="unidades_vendidas">Unidades vendidas</option>
              <option value="ingresos">Ingresos</option>
              <option value="beneficio">Beneficio</option>
              <option value="rotacion">Rotación</option>
            </select>
          </label>
          <label>Top N:
            <select id="grafProductosTop">
              <option value="5">5</option>
              <option value="10" selected>10</option>
              <option value="15">15</option>
              <option value="20">20</option>
            </select>
          </label>
        </div>
        <canvas id="chartProductos"></canvas>
      </div>
    </section>

    <!-- Comentario automático -->
    <section class="section">
      <div class="card">
        <h2>Comentario automático del negocio</h2>
        <p id="comentarioNegocio">
          Suba un CSV para ver el análisis del estanco.
        </p>
      </div>
    </section>
  </main>

  <!-- Lógica JS -->
  <script>
    let datos = [];

    // Márgenes estándar por categoría (como en la app previa)
    const MARGENES = {
      tabaco_cajetilla: 0.085,
      tabaco_rollo: 0.09,
      puros: 0.09,
      sellos: 0.04,
      otros: 0.20
    };

    // Función simple para parsear CSV (cabeceras + filas)
    function parseCSV(text) {
      const lines = text.trim().split("\\n");
      const headers = lines[0].split(",").map(h => h.trim());
      const rows = lines.slice(1);
      return rows.map(line => {
        const values = line.split(",").map(v => v.trim());
        const row = {};
        headers.forEach((h, i) => {
          row[h] = values[i];
        });
        return row;
      });
    }

    // Calcular métricas
    function prepararDatos(raw) {
      return raw.map(row => {
        const unidades = Number(row.unidades_vendidas || 0);
        const precio = Number(row.precio_venta_unitario || 0);
        const stock = Number(row.stock_medio || 0);
        const ingresos = unidades * precio;
        const margenPct = MARGENES[row.categoria] ?? 0.20;
        const beneficio = ingresos * margenPct;
        const rotacion = stock > 0 ? unidades / stock : 0;

        return {
          producto: row.producto || "",
          categoria: row.categoria || "",
          unidades_vendidas: unidades,
          precio_venta_unitario: precio,
          stock_medio: stock,
          ingresos,
          margen_pct: margenPct,
          beneficio,
          rotacion
        };
      });
    }

    // Renderizar tabla genérica
    function renderTable(containerId, rows, columns) {
      const container = document.getElementById(containerId);
      if (!rows || rows.length === 0) {
        container.innerHTML = "<p>No hay datos.</p>";
        return;
      }
      let html = "<table><thead><tr>";
      columns.forEach(col => {
        html += `<th>${col.label}</th>`;
      });
      html += "</tr></thead><tbody>";
      rows.forEach(r => {
        html += "<tr>";
        columns.forEach(col => {
          html += `<td>${col.format ? col.format(r[col.key]) : r[col.key]}</td>`;
        });
        html += "</tr>";
      });
      html += "</tbody></table>";
      container.innerHTML = html;
    }

    // KPIs
    function actualizarKPIs() {
      const ingresosTotales = datos.reduce((acc, r) => acc + r.ingresos, 0);
      const beneficioTotal = datos.reduce((acc, r) => acc + r.beneficio, 0);
      const rotacionMedia = datos.length
        ? datos.reduce((acc, r) => acc + r.rotacion, 0) / datos.length
        : 0;

      document.getElementById("kpiIngresos").textContent =
        ingresosTotales.toLocaleString("es-ES", { maximumFractionDigits: 2 }) + " €";
      document.getElementById("kpiBeneficio").textContent =
        beneficioTotal.toLocaleString("es-ES", { maximumFractionDigits: 2 }) + " €";
      document.getElementById("kpiRotacion").textContent =
        rotacionMedia.toLocaleString("es-ES", { maximumFractionDigits: 2 }) + " veces";
    }

    // Tablas
    function actualizarTablas() {
      // Resumen
      renderTable("tablaResumen", datos, [
        { key: "producto", label: "Producto" },
        { key: "categoria", label: "Categoría" },
        { key: "unidades_vendidas", label: "Unidades" },
        { key: "precio_venta_unitario", label: "Precio (€)" },
        { key: "ingresos", label: "Ingresos (€)", format: v => v.toLocaleString("es-ES", { maximumFractionDigits: 2 }) },
        { key: "beneficio", label: "Beneficio (€)", format: v => v.toLocaleString("es-ES", { maximumFractionDigits: 2 }) },
        { key: "rotacion", label: "Rotación", format: v => v.toLocaleString("es-ES", { maximumFractionDigits: 2 }) }
      ]);

      // Ranking productos
      const metric = document.getElementById("rankingMetric").value;
      const topN = Number(document.getElementById("rankingTop").value);
      const ordenados = [...datos].sort((a, b) => b[metric] - a[metric]).slice(0, topN);
      renderTable("tablaProductos", ordenados, [
        { key: "producto", label: "Producto" },
        { key: "categoria", label: "Categoría" },
        { key: "unidades_vendidas", label: "Unidades" },
        { key: "ingresos", label: "Ingresos (€)", format: v => v.toLocaleString("es-ES", { maximumFractionDigits: 2 }) },
        { key: "beneficio", label: "Beneficio (€)", format: v => v.toLocaleString("es-ES", { maximumFractionDigits: 2 }) },
        { key: "rotacion", label: "Rotación", format: v => v.toLocaleString("es-ES", { maximumFractionDigits: 2 }) }
      ]);

      // Categorías
      const categorias = {};
      datos.forEach(r => {
        if (!categorias[r.categoria]) {
          categorias[r.categoria] = {
            categoria: r.categoria,
            ingresos_total: 0,
            beneficio_total: 0,
            unidades_total: 0,
            rotacion_media: 0,
            conteo: 0
          };
        }
        const c = categorias[r.categoria];
        c.ingresos_total += r.ingresos;
        c.beneficio_total += r.beneficio;
        c.unidades_total += r.unidades_vendidas;
        c.rotacion_media += r.rotacion;
        c.conteo += 1;
      });
      const filasCat = Object.values(categorias).map(c => ({
        categoria: c.categoria,
        ingresos_total: c.ingresos_total,
        beneficio_total: c.beneficio_total,
        unidades_total: c.unidades_total,
        rotacion_media: c.conteo ? c.rotacion_media / c.conteo : 0
      }));
      renderTable("tablaCategorias", filasCat, [
        { key: "categoria", label: "Categoría" },
        { key: "ingresos_total", label: "Ingresos (€)", format: v => v.toLocaleString("es-ES", { maximumFractionDigits: 2 }) },
        { key: "beneficio_total", label: "Beneficio (€)", format: v => v.toLocaleString("es-ES", { maximumFractionDigits: 2 }) },
        { key: "unidades_total", label: "Unidades" },
        { key: "rotacion_media", label: "Rotación media", format: v => v.toLocaleString("es-ES", { maximumFractionDigits: 2 }) }
      ]);

      // Comentario negocio
      if (filasCat.length > 0) {
        const topIngresos = filasCat.reduce((a, b) => (b.ingresos_total > a.ingresos_total ? b : a), filasCat[0]);
        const topBeneficio = filasCat.reduce((a, b) => (b.beneficio_total > a.beneficio_total ? b : a), filasCat[0]);
        const comentario = `
El estanco genera unos ingresos totales aproximados de ${datos.reduce((acc, r) => acc + r.ingresos, 0).toLocaleString("es-ES", { maximumFractionDigits: 2 })} €,
con un beneficio estimado de ${datos.reduce((acc, r) => acc + r.beneficio, 0).toLocaleString("es-ES", { maximumFractionDigits: 2 })} €.

La categoría con mayor peso en ingresos es "${topIngresos.categoria}", mientras que la que más contribuye al beneficio es "${topBeneficio.categoria}".
La rotación media indica cuántas veces se renueva el stock; una rotación alta sugiere productos de venta rápida y una rotación baja apunta a artículos que permanecen más tiempo en estantería.

Con esta información se pueden identificar oportunidades para potenciar referencias de alta rentabilidad, reducir productos de baja rotación y optimizar la mezcla de complementos para aumentar el margen global del estanco.
`;
        document.getElementById("comentarioNegocio").textContent = comentario;
      }
    }

    // Gráficos
    let chartCategorias = null;
    let chartProductos = null;

    function actualizarGraficos() {
      const categorias = {};
      datos.forEach(r => {
        if (!categorias[r.categoria]) {
          categorias[r.categoria] = {
            ingresos_total: 0,
            beneficio_total: 0,
            unidades_total: 0
          };
        }
        const c = categorias[r.categoria];
        c.ingresos_total += r.ingresos;
        c.beneficio_total += r.beneficio;
        c.unidades_total += r.unidades_vendidas;
      });
      const filasCat = Object.entries(categorias).map(([cat, v]) => ({
        categoria: cat,
        ...v
      }));

      const metricCat = document.getElementById("grafCategoriaMetric").value;
      const labelsCat = filasCat.map(f => f.categoria);
      const dataCat = filasCat.map(f => f[metricCat]);

      const ctxCat = document.getElementById("chartCategorias").getContext("2d");
      if (chartCategorias) chartCategorias.destroy();
      chartCategorias = new Chart(ctxCat, {
        type: "bar",
        data: {
          labels: labelsCat,
          datasets: [
            {
              label: metricCat,
              data: dataCat,
              backgroundColor: "#2563eb"
            }
          ]
        },
        options: {
          plugins: { legend: { display: false } },
          scales: {
            x: { ticks: { color: "#9ca3af" } },
            y: { ticks: { color: "#9ca3af" } }
          }
        }
      });

      const metricProd = document.getElementById("grafProductosMetric").value;
      const topN = Number(document.getElementById("grafProductosTop").value);
      const ordenados = [...datos].sort((a, b) => b[metricProd] - a[metricProd]).slice(0, topN);

      const labelsProd = ordenados.map(r => r.producto);
      const dataProd = ordenados.map(r => r[metricProd]);

      const ctxProd = document.getElementById("chartProductos").getContext("2d");
      if (chartProductos) chartProductos.destroy();
      chartProductos = new Chart(ctxProd, {
        type: "bar",
        data: {
          labels: labelsProd,
          datasets: [
            {
              label: metricProd,
              data: dataProd,
              backgroundColor: "#22c55e"
            }
          ]
        },
        options: {
          plugins: { legend: { display: false } },
          scales: {
            x: { ticks: { color: "#9ca3af" } },
            y: { ticks: { color: "#9ca3af" } }
          }
        }
      });
    }

    // Tabs
    document.querySelectorAll(".tab-button").forEach(btn => {
      btn.addEventListener("click", () => {
        const tab = btn.dataset.tab;
        document.querySelectorAll(".tab-button").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        document.getElementById("tabResumen").style.display = tab === "resumen" ? "" : "none";
        document.getElementById("tabProductos").style.display = tab === "productos" ? "" : "none";
        document.getElementById("tabCategorias").style.display = tab === "categorias" ? "" : "none";
        document.getElementById("tabGraficos").style.display = tab === "graficos" ? "" : "none";
      });
    });

    // Eventos de controles
    document.getElementById("rankingMetric").addEventListener("change", () => {
      actualizarTablas();
    });
    document.getElementById("rankingTop").addEventListener("change", () => {
      actualizarTablas();
    });
    document.getElementById("grafCategoriaMetric").addEventListener("change", () => {
      actualizarGraficos();
    });
    document.getElementById("grafProductosMetric").addEventListener("change", () => {
      actualizarGraficos();
    });
    document.getElementById("grafProductosTop").addEventListener("change", () => {
      actualizarGraficos();
    });

    // Subida de CSV
    document.getElementById("fileInput").addEventListener("change", e => {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = event => {
        const raw = parseCSV(event.target.result);
        datos = prepararDatos(raw);
        actualizarKPIs();
        actualizarTablas();
        actualizarGraficos();
      };
      reader.readAsText(file, "UTF-8");
    });

    // Cargar datos de ejemplo al iniciar (opcional)
    const datosEjemplo = prepararDatos([
      {
        producto: "Marlboro Rojo 20",
        categoria: "tabaco_cajetilla",
        unidades_vendidas: 1200,
        precio_venta_unitario: 5.5,
        stock_medio: 150
      },
      {
        producto: "Camel Blue 20",
        categoria: "tabaco_cajetilla",
        unidades_vendidas: 900,
        precio_venta_unitario: 5.3,
        stock_medio: 120
      },
      {
        producto: "Mecheros BIC",
        categoria: "otros",
        unidades_vendidas: 250,
        precio_venta_unitario: 1.5,
        stock_medio: 30
      }
    ]);
    datos = datosEjemplo;
    actualizarKPIs();
    actualizarTablas();
    actualizarGraficos();
  </script>
</body>
</html>
