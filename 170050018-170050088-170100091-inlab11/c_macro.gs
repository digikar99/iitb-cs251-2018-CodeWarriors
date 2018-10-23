function MD5 (input) {
  var rawHash = Utilities.computeDigest(Utilities.DigestAlgorithm.MD5, input);
  var txtHash = '';
  for (i = 0; i < rawHash.length; i++) {
    var hashVal = rawHash[i];
    if (hashVal < 0) {
      hashVal += 256;
    }
    if (hashVal.toString(16).length == 1) {
      txtHash += '0';
    }
    txtHash += hashVal.toString(16);
  }
  return txtHash;
}


function myFunction1() {
  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getCurrentCell().offset(0, 1).activate();
  spreadsheet.getCurrentCell().setFormulaR1C1('=Md5(R[0]C[-1])');
  spreadsheet.getRange('D1').activate();
  spreadsheet.getCurrentCell().setValue('Checksum_Input');
  spreadsheet.getRange('G1').activate();
  spreadsheet.getCurrentCell().setValue('md5checksum');
  spreadsheet.getRange('G2').activate();
  spreadsheet.getCurrentCell().setFormula('=MD5(D2)');
  spreadsheet.getActiveRange().autoFill(spreadsheet.getRange('G2:G126'), SpreadsheetApp.AutoFillSeries.DEFAULT_SERIES);
  spreadsheet.getRange('G2:G126').activate();
};