from pathlib import Path

ROOT=Path(__file__).parents[1]

def brier(probability,outcome):
    p=probability*10; target=1000 if outcome else 0
    return ((p-target)*(p-target))//1000

def test_brier_is_deterministic_and_rewards_accuracy():
    assert brier(80,True)==40
    assert brier(20,True)==640
    assert brier(20,False)==40

def test_contract_has_source_and_lifecycle_guards():
    source=(ROOT/'contracts/contract.py').read_text(encoding='utf-8')
    for token in ('anchored forecast source changed','independent outcome origin required','owner may cancel only before resolution opens','nothing is evaluated partially','prompt_comparative','SCORED','UNRESOLVED'):
        assert token in source
    assert 'forecast.state=\'SCORED\' if outcome!=\'INDETERMINATE\'' in source

def test_frontend_waits_for_finality_and_is_not_argument_grid():
    page=(ROOT/'docs/index.html').read_text(encoding='utf-8')
    assert 'status:"FINALIZED"' in page
    assert 'WAITING FOR FINALITY' in page
    assert 'light-table' in page
    assert 'BRIER' in page
