import sys
import unittest

from flexmock import flexmock
from conditional import conditional


class ConditionalTests(unittest.TestCase):

    def make_one(self, **kw):
        attrs = dict(__enter__=lambda:None, __exit__=lambda x,y,z:None)
        attrs.update(kw)
        return flexmock(**attrs)

    def test_true_condition_enters_context_manager(self):
        cm = self.make_one()
        flexmock(cm).should_call('__enter__').once()
        flexmock(cm).should_call('__exit__').once()

        with conditional(True, cm):
            pass

    def test_false_condition_does_not_enter_context_manager(self):
        cm = self.make_one()
        flexmock(cm).should_call('__enter__').never()
        flexmock(cm).should_call('__exit__').never()

        with conditional(False, cm):
            pass

    def test_true_condition_returns_enter_result(self):
        cm = self.make_one(__enter__=lambda:42)
        flexmock(cm).should_call('__enter__').once()
        flexmock(cm).should_call('__exit__').once()

        with conditional(True, cm) as value:
            self.assertEqual(value, 42)

    def test_false_condition_returns_None(self):
        cm = self.make_one()
        flexmock(cm).should_call('__enter__').never()
        flexmock(cm).should_call('__exit__').never()

        with conditional(False, cm) as value:
            self.assertEqual(value, None)

    def test_returning_true_from_exit_handles_exception(self):
        cm = self.make_one(__exit__=lambda x,y,z:True)
        flexmock(cm).should_call('__enter__').once()
        flexmock(cm).should_call('__exit__').once()

        with conditional(True, cm):
            raise RuntimeError()

    def test_returning_None_from_exit_lets_exception_propagate(self):
        cm = self.make_one()
        flexmock(cm).should_call('__enter__').once()
        flexmock(cm).should_call('__exit__').once()

        try:
            with conditional(True, cm):
                raise RuntimeError()
        except RuntimeError:
            pass # success
        else:
            self.fail('RuntimeError not raised')


if sys.version_info >= (3, 8):
    from unittest.mock import AsyncMock


    class AsyncConditionalTests(unittest.IsolatedAsyncioTestCase):

        def make_one(self, **kw):
            attrs = dict(__aenter__=AsyncMock(return_value=None), __aexit__=AsyncMock(return_value=None))
            attrs.update(kw)
            return flexmock(**attrs)

        async def test_true_condition_enters_context_manager(self):
            cm = self.make_one()
            flexmock(cm).should_call('__aenter__').once()
            flexmock(cm).should_call('__aexit__').once()

            async with conditional(True, cm):
                pass

        async def test_false_condition_does_not_enter_context_manager(self):
            cm = self.make_one()
            flexmock(cm).should_call('__aenter__').never()
            flexmock(cm).should_call('__aexit__').never()

            async with conditional(False, cm):
                pass

        async def test_true_condition_returns_enter_result(self):
            cm = self.make_one(__aenter__=AsyncMock(return_value=42))
            flexmock(cm).should_call('__aenter__').once()
            flexmock(cm).should_call('__aexit__').once()

            async with conditional(True, cm) as value:
                self.assertEqual(value, 42)

        async def test_false_condition_returns_None(self):
            cm = self.make_one()
            flexmock(cm).should_call('__aenter__').never()
            flexmock(cm).should_call('__aexit__').never()

            async with conditional(False, cm) as value:
                self.assertEqual(value, None)

        async def test_returning_true_from_exit_handles_exception(self):
            cm = self.make_one(__aexit__=AsyncMock(return_value=True))
            flexmock(cm).should_call('__aenter__').once()
            flexmock(cm).should_call('__aexit__').once()

            async with conditional(True, cm):
                raise RuntimeError()

        async def test_returning_None_from_exit_lets_exception_propagate(self):
            cm = self.make_one()
            flexmock(cm).should_call('__aenter__').once()
            flexmock(cm).should_call('__aexit__').once()

            try:
                async with conditional(True, cm):
                    raise RuntimeError()
            except RuntimeError:
                pass # success
            else:
                self.fail('RuntimeError not raised')

