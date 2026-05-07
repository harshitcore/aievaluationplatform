// Ensure only one model can be marked as 'Best'
function toggleBest(modelId) {
    if (modelId === 'A' && document.getElementById('bestA').checked) {
        document.getElementById('bestB').checked = false;
    } else if (modelId === 'B' && document.getElementById('bestB').checked) {
        document.getElementById('bestA').checked = false;
    }
}

let generatedContentA = "";
let generatedContentB = "";

function generateResponses() {
    const prompt = document.getElementById('promptInput').value.trim();
    if (!prompt) {
        alert("Please enter a prompt first.");
        return;
    }

    const btn = document.getElementById('generateBtn');
    const loading = document.getElementById('loadingIndicator');
    const evalSection = document.getElementById('evaluationSection');

    btn.disabled = true;
    loading.style.display = 'inline-block';
    evalSection.style.display = 'none';

    fetch('/eval/api/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: prompt })
    })
    .then(response => response.json())
    .then(data => {
        generatedContentA = data.model_a;
        generatedContentB = data.model_b;
        
        document.getElementById('responseA').textContent = generatedContentA;
        document.getElementById('responseB').textContent = generatedContentB;
        
        evalSection.style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while generating responses.');
    })
    .finally(() => {
        btn.disabled = false;
        loading.style.display = 'none';
    });
}

function submitEvaluation(projectId) {
    const prompt = document.getElementById('promptInput').value.trim();
    
    // Construct response objects
    const responses = [
        {
            model_name: 'Model A',
            content: generatedContentA,
            score_accuracy: parseInt(document.getElementById('score_acc_a').value),
            score_relevance: parseInt(document.getElementById('score_rel_a').value),
            score_clarity: parseInt(document.getElementById('score_clarity_a').value),
            score_completeness: parseInt(document.getElementById('score_comp_a').value),
            score_safety: parseInt(document.getElementById('score_safe_a').value),
            is_best: document.getElementById('bestA').checked,
            is_hallucination: document.getElementById('hallucinationA').checked,
            feedback: document.getElementById('feedbackA').value
        },
        {
            model_name: 'Model B',
            content: generatedContentB,
            score_accuracy: parseInt(document.getElementById('score_acc_b').value),
            score_relevance: parseInt(document.getElementById('score_rel_b').value),
            score_clarity: parseInt(document.getElementById('score_clarity_b').value),
            score_completeness: parseInt(document.getElementById('score_comp_b').value),
            score_safety: parseInt(document.getElementById('score_safe_b').value),
            is_best: document.getElementById('bestB').checked,
            is_hallucination: document.getElementById('hallucinationB').checked,
            feedback: document.getElementById('feedbackB').value
        }
    ];

    const btn = document.getElementById('submitEvalBtn');
    const originalText = btn.innerHTML;
    btn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Submitting...';
    btn.disabled = true;

    fetch('/eval/api/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            project_id: projectId,
            prompt: prompt,
            responses: responses
        })
    })
    .then(response => response.json())
    .then(data => {
        if(data.message) {
            window.location.href = '/dashboard';
        } else {
            alert('Error: ' + data.error);
            btn.innerHTML = originalText;
            btn.disabled = false;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred during submission.');
        btn.innerHTML = originalText;
        btn.disabled = false;
    });
}
