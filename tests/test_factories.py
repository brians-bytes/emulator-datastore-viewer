import factory
from  factory import fuzzy
from viewer.models.kind import KindModel


class KindFactory(factory.Factory):
    class Meta:
        model = KindModel
        inline_args = ['kind', 'namespace']

    kind = fuzzy.FuzzyChoice([f'sample_kind_{i}' for i in range(3)])
    namespace = fuzzy.FuzzyChoice([None, 'namespace_1'])
    __attr = {
        'name': 'brian',
        'property': 'test',
    }
