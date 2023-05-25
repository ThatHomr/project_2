const goYear = () => {
  let fm = document.getElementById("fm");
  const name = fm.name.value;
  const year = fm.year_data.value;
  const area = fm.area_data.value;
  let url = "";
  alert("name : " + name);
  if (name == "지방세") {
    url = "/yearmap/local/?year=" + year + "&area=" + area;
  } else if (name == "지역내생산(grdp)") {
    url = "/yearmap/grdp/?year=" + year + "&area=" + area;
  } else if (name == "공장면적") {
    url = "/yearmap/factory/?year=" + year + "&area=" + area;
  } else if (name == "의료인수") {
    url = "/yearmap/medical/?year=" + year + "&area=" + area;
  } else if (name == "병동수") {
    url = "/yearmap/hospital/?year=" + year + "&area=" + area;
  }
  fm.action = url;
  fm.submit();
};

const init_year_selected = (year_data) => {
  fm = document.getElementById("fm");
  for (i = 0; i < fm.year_data.options.length; i++) {
    // 저장 데이터와 같은 option 선택하기
    if (fm.year_data.options[i].value == year_data) {
      fm.year_data.options[i].selected = true;
      break;
    }
  }
};

const init_area_selected = (area_data) => {
  fm = document.getElementById("fm");
  for (i = 0; i < fm.area_data.options.length; i++) {
    // 저장 데이터와 같은 option 선택하기
    if (fm.area_data.options[i].value == area_data) {
      fm.area_data.options[i].selected = true;
      break;
    }
  }
};
