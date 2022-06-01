import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, cohen_kappa_score, roc_curve, auc
from sklearn.model_selection import cross_validate, RepeatedStratifiedKFold

# Custom function to print the metrics of the model


def metrics_summary(y_test, y_pred, y_prob):
    print(confusion_matrix(y_test, y_pred))
    print('=================================================')
    print(f'Kappa Score: {cohen_kappa_score(y_test, y_pred)}')
    print(f'Accuracy Score: {accuracy_score(y_test, y_pred)}')
    print(f'Precision: {precision_score(y_test, y_pred)}')
    print(f'Recall: {recall_score(y_test, y_pred)}')
    print(f'F1 Score: {f1_score(y_test, y_pred)}')
    print(f'AUC Score: {roc_auc_score(y_test, y_prob)}')
    print('=================================================')


def crossval_summary(model, X_train, y_train):
    scoring = ['accuracy', 'precision', 'recall', 'f1_micro', 'roc_auc']
    cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=1)

    results = cross_validate(model, X_train, y_train, scoring=scoring, cv=cv)
    print('=================================================')
    print(f"Average Accuracy Score: {np.mean(results['test_accuracy'])}")
    print(f"Average Precision Score: {np.mean(results['test_precision'])}")
    print(f"Average Recall Score: {np.mean(results['test_recall'])}")
    print(f"Average F1 Score: {np.mean(results['test_f1_micro'])}")
    print(results['test_f1_micro'])
    print(f"Average AUC Score: {np.mean(results['test_roc_auc'])}")
    print(results['test_roc_auc'])
    print('=================================================')


def plot_roc(model, name, X_test, y_test):
    # calculate the fpr and tpr for all thresholds of the classification
    probs = model.predict_proba(X_test)
    preds = probs[:, 1]
    fpr, tpr, threshold = roc_curve(y_test, preds)
    roc_auc = auc(fpr, tpr)

    # method I: plt
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.plot(fpr, tpr, 'b', label=f'{name} = {roc_auc:0.4f}', linewidth=2)
    ax.legend(loc='lower right')
    ax.plot([0, 1], [0, 1], 'r--')
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1.01])
    ax.set_xlabel('False Positive Rate', fontsize=14)
    ax.set_ylabel('True Positive Rate', fontsize=14)
    ax.set_title(f'ROC Curve for {name}', fontsize=20)
    ax.legend(loc="lower right", title="AUC", fontsize=12)
    plt.show()
