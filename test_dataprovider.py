import pandas as pd
import pytest

claims = pd.read_csv(r'.\raw_data\sample_claims.csv')

def test_claim_id_is_unique():
	assert not claims.duplicated(subset=['claim_id']).any()

def test_diagnosis_code_is_not_empty():
	assert not claims['diagnosis_codes'].str.strip().eq('').any()

def test_diagnosis_code_is_not_null():
	assert not claims['diagnosis_codes'].isnull().values.any()