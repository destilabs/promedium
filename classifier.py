from functools import partial
import pandas as pd
from tqdm import tqdm

from transformers import pipeline
from transformers.pipelines.pt_utils import KeyDataset

import argparse

from functools import partial

class TitleClassifier:
    def __init__(self, labels):
        self.labels = labels
        self.pipeline = pipeline('zero-shot-classification')

    def predict(self, text):
        return self.pipeline(text, self.labels)

if __name__ == '__main__':
    tqdm.pandas()

    parser = argparse.ArgumentParser()

    parser.add_argument('--data_path', type=str, default='./outputs/output.csv', help='Path to the data')
    parser.add_argument('--predictions_output', type=str, default='./outputs/predictions.csv', help='Path to the predictions output')
    parser.add_argument('--num_of_titles', type=int, default=10, help='Number of titles to classify')
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size')
    parser.add_argument('--output_path', type=str, default='./outputs/output.png', help='Path to the output')

    args = parser.parse_args()

    reading_list = pd.read_csv(args.data_path).head(args.num_of_titles)

    labels = reading_list['Tags'].unique()

    clf = TitleClassifier(labels)

    results = []
    sequences = reading_list['Title'].to_list()

    for i in tqdm(range(0, len(reading_list), args.batch_size)):
        results.extend(clf.predict(sequences[i:i+args.batch_size]))

    reading_list['Predictions'] = [x['labels'][0] for x in results]
    reading_list['Predictions'].value_counts().plot(kind = 'barh', figsize = (20, 10)).get_figure().savefig(args.output_path)

    reading_list.to_csv(args.predictions_output, index=False)