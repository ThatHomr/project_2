const goYear = () => {
  let fm = document.getElementById("fm");

  const year_data = fm.year_data.value;
  const name = fm.name.value;
  let url = "";

  alert("name : " + name);
  if (name == "소비자물가지수") {
    url = "/yeargraph/price_view/?year_data=" + year_data;
  } else if (name == "코스피") {
    url = "/yeargraph/price_view/?year_data=" + year_data;
  } else if (name == "고용률") {
    url = "/yeargraph/price_view/?year_data=" + year_data;
  } else if (name == "관광객수") {
    url = "/yeargraph/price_view/?year_data=" + year_data;
  } else if (name == "주택가격") {
    url = "/yeargraph/price_view/?year_data=" + year_data;
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
