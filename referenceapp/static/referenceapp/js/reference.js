const goYear = () => {
  let fm = document.getElementById("fm");

  // 상품분류 selectbox가 선택이 되면..
  // - 상품코드의 값은 초기화("") 시켜야함
  const year = fm.year_data.value;
  const month = fm.month_data.value;
  let url = "/rederence/map_view/?year=" + year + "&month=" + month;
  alert("year: " + year + " month: " + month + " url: " + url);
  fm.action = url;
  fm.submit();
};

const init_lpord_selected = (year_data) => {
  fm = document.getElementById("fm");
  for (i = 0; i < fm.lprod_gu.options.length; i++) {
    // 저장 데이터와 같은 option 선택하기
    if (fm.lprod_gu.options[i].value == year_data) {
      fm.year_data.options[i].selected = true;
      break;
    }
  }
};

const init_pord_selected = (month_data) => {
  fm = document.getElementById("fm");
  for (i = 0; i < fm.month_data.options.length; i++) {
    // 저장 데이터와 같은 option 선택하기
    if (fm.month_data.options[i].value == prod_id) {
      fm.month_data.options[i].selected = true;
      break;
    }
  }
};
