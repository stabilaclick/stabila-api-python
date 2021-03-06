# --------------------------------------------------------------------
# Copyright (c) stabilaclick. All rights reserved.
# Licensed under the MIT License.
# See License.txt in the project root for license information.
# --------------------------------------------------------------------


class Module:
    """Module Class"""

    def __init__(self, stabila) -> None:
        self.stabila = stabila

    @classmethod
    def attach(cls, target, module_name: str = None) -> None:
        if not module_name:
            module_name = cls.__name__.lower()

        if hasattr(target, module_name):
            raise AttributeError(
                "Cannot set {0} module named '{1}'.  The stabila object "
                "already has an attribute with that name".format(
                    target,
                    module_name,
                )
            )

        if isinstance(target, Module):
            stabila = target.stabila
        else:
            stabila = target

        setattr(target, module_name, cls(stabila))
