let currentAst = null; // Variable to store the current AST

function createRule() {
  const ruleExpression = document.getElementById("ruleExpression").value;
  fetch("/create_rule", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ rule: ruleExpression }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.ast) {
        currentAst = data.ast; // Store the AST in the variable
        document.getElementById("rule-ast").innerText = JSON.stringify(
          data.ast,
          null,
          2
        );
      } else {
        document.getElementById("rule-ast").innerText = `Error: ${data.error}`;
      }
    })
    .catch((error) => console.error("Error:", error));
}

function evaluateRule() {
  const data = {
    age: Number(document.getElementById("age").value),
    department: document.getElementById("department").value,
    salary: Number(document.getElementById("salary").value),
    experience: Number(document.getElementById("experience").value) || 0, // Default to 0 if empty
  };

  if (!currentAst) {
    document.getElementById("evaluation-result").innerText =
      "Error: No AST available. Please create a rule first.";
    return;
  }

  fetch("/evaluate_rule", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ data, ast: currentAst }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById(
        "evaluation-result"
      ).innerText = `Result: ${data.result}`;
    })
    .catch((error) => console.error("Error:", error));
}
