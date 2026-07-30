---
title: Essence Guaranteed Modifiers
---

# Essence Guaranteed Modifiers

Pick an item class to see every essence and what it guarantees on that item class. Data comes from the vendored RePoE snapshot (see `data/repoe/SOURCE.md` in the repo).

Mod names below are cleaned-up internal mod ids, not exact in-game wording. Treat them as "what kind of modifier", not "the exact tooltip text".

<div id="essence-table-app">
  <label for="item-class-select">Item class:</label>
  <select id="item-class-select"></select>
  <table id="essence-table">
    <thead>
      <tr>
        <th>Essence</th>
        <th>Tier</th>
        <th>Corruption only</th>
        <th>Item level cap</th>
        <th>Guaranteed modifier</th>
      </tr>
    </thead>
    <tbody id="essence-table-body"></tbody>
  </table>
</div>

<script>
(function () {
  fetch("../essences-data.json")
    .then(function (res) { return res.json(); })
    .then(function (essences) {
      var select = document.getElementById("item-class-select");
      var body = document.getElementById("essence-table-body");

      var itemClasses = new Set();
      essences.forEach(function (e) {
        Object.keys(e.mods).forEach(function (ic) { itemClasses.add(ic); });
      });
      var sortedClasses = Array.from(itemClasses).sort();

      sortedClasses.forEach(function (ic) {
        var opt = document.createElement("option");
        opt.value = ic;
        opt.textContent = ic;
        select.appendChild(opt);
      });

      function render(itemClass) {
        body.innerHTML = "";
        var rows = essences.filter(function (e) { return itemClass in e.mods; });
        function familyOf(name) {
          var idx = name.indexOf(" of ");
          return idx === -1 ? name : name.slice(idx + 4);
        }
        rows.sort(function (a, b) {
          var fa = familyOf(a.name), fb = familyOf(b.name);
          if (fa !== fb) return fa < fb ? -1 : 1;
          return (a.tier || 0) - (b.tier || 0);
        });
        rows.forEach(function (e) {
          var tr = document.createElement("tr");
          var cap = e.item_level_cap === null ? "none" : e.item_level_cap;
          var tier = e.tier === null ? "-" : e.tier;
          tr.innerHTML =
            "<td>" + e.name + "</td>" +
            "<td>" + tier + "</td>" +
            "<td>" + (e.corruption_only ? "yes" : "") + "</td>" +
            "<td>" + cap + "</td>" +
            "<td>" + e.mods[itemClass] + "</td>";
          body.appendChild(tr);
        });
      }

      var defaultClass = sortedClasses.includes("Boots") ? "Boots" : sortedClasses[0];
      select.value = defaultClass;
      render(defaultClass);

      select.addEventListener("change", function () {
        render(select.value);
      });
    });
})();
</script>
