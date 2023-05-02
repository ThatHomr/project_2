const goYear = () => {
  let fm = document.getElementById("fm");

  const year_data = fm.year_data.value;
  const month_data = fm.month_data.value;
  const area_data = fm.area_data.value;
  let url =
    "/people/people_num/?year_data=" +
    year_data +
    "&month_data=" +
    month_data +
    "&area_data=" +
    area_data;
  alert(
    "year: " +
      year_data +
      " month: " +
      month_data +
      " area: " +
      area_data +
      " url: " +
      url
  );
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

const init_month_selected = (month_data) => {
  fm = document.getElementById("fm");
  for (i = 0; i < fm.month_data.options.length; i++) {
    // 저장 데이터와 같은 option 선택하기
    if (fm.month_data.options[i].value == month_data) {
      fm.month_data.options[i].selected = true;
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
